import re
import os
import shutil
import yaml
import json
from loguru import logger
import time

def fuzzyfinder(user_input, collection): # 模糊搜索
    suggestions = []
    pattern = '.*'.join(user_input) # Converts 'djm' to 'd.*j.*m'
    regex = re.compile(pattern)     # Compiles a regex.
    for item in collection:
        match = regex.search(item)  # Checks if the current item matches the regex.
        if match:
            suggestions.append(item)
    if suggestions != []:
        return suggestions
    else:
        return False

up_yaml = open("/py/Emby-FDAC/set.yml","rb")
up_set_json = yaml.load(up_yaml.read(),Loader=yaml.FullLoader)
up_yaml.close()
logger.info("读取配置文件")

up_input_dir = up_set_json["in_dir"]
up_move_out_dir = up_set_json["out_dir"]



logger.info("读取番剧列表")
up_fan_list_json = open("/py/Emby-FDAC/fan.json","rb")
up_fan_list_json = json.loads(up_fan_list_json.read())
#print(up_fan_list_json["1"]["name"])
logger.info("读取临时文件列表")
up_load_input_dir = os.listdir(up_input_dir)
for name_list in up_fan_list_json:
    for name_list_name in up_fan_list_json[name_list]["name"]:
        see_file_name = fuzzyfinder(up_fan_list_json[name_list]["name"][name_list_name], up_load_input_dir)
        if see_file_name is False:
            break
        #print(see_file_name)
        logger.info("移动: "+see_file_name[0]+"->"+up_fan_list_json[name_list]["out_dir"])
        logger.info(up_input_dir+"/"+see_file_name[0]+" 移动到 "+up_fan_list_json[name_list]["out_dir"])
        if os.path.isdir(up_move_out_dir+"/"+up_fan_list_json[name_list]["out_dir"]) is False:
            os.mkdir(up_move_out_dir+"/"+up_fan_list_json[name_list]["out_dir"])
        if os.path.isdir(up_move_out_dir+"/"+up_fan_list_json[name_list]["out_dir"]+"/Season "+up_fan_list_json[name_list]["season"]) is False:
            os.mkdir(up_move_out_dir+"/"+up_fan_list_json[name_list]["out_dir"]+"/Season "+up_fan_list_json[name_list]["season"])
        shutil.move(up_input_dir+"/"+see_file_name[0],up_move_out_dir+"/"+up_fan_list_json[name_list]["out_dir"]+"/Season "+up_fan_list_json[name_list]["season"])
        logger.info("运行重命名脚本")
        time.sleep(10)
        os.system('python3 "/py/Emby-FDAC/Re_name/EpisodeReName.py" "'+up_move_out_dir+'/'+up_fan_list_json[name_list]["out_dir"]+'"')
        logger.info("文件 "+see_file_name[0]+" 移动完成")
		

time.sleep(10)
os.system('python3 "/py/Emby-FDAC/Re_name/EpisodeReName.py" "'+up_move_out_dir+'/"')


