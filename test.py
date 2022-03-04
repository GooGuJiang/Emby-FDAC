import re
import os
import shutil
from turtle import up
import yaml
import json
from loguru import logger

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

up_yaml = open("./set.yml","rb")
up_set_json = yaml.load(up_yaml.read(),Loader=yaml.FullLoader)
up_yaml.close()
logger.info("读取配置文件")

up_input_dir = up_set_json["in_dir"]
up_move_out_dir = up_set_json["out_dir"]



logger.info("读取番剧列表")
up_fan_list_json = open("./fan.json","rb")
up_fan_list_json = json.loads(up_fan_list_json.read())
print(up_fan_list_json["1"]["name"])


