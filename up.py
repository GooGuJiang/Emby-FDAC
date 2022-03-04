import sys
import getopt
import telebot
import os
from urllib.parse import quote
import time

bot = telebot.TeleBot("#", parse_mode=None)# Telegram 推送消息用
#apihelper.proxy = {'https':'socks5://127.0.0.1:8089'}


def guup():
    name = None
 
    argv = sys.argv[1:]
 
    try:
        opts, args = getopt.getopt(argv, "i:")  # 短选项模式
     
    except:
        print("Error")
 
    for opt, arg in opts:
        if opt in ['-i']:
            name = arg
    okname = name[16:len(name)]
    try:
        text = bot.send_message("@Gu_Fan","开始上传【"+okname+"】到 OneDrive 中...")
        #shutil.move(name,"/root/OneDrive/Bangumi")
        os.system('rclone copy "'+name+'" onedrive:/tmp')
        #bot.edit_message_text("【"+okname+"】上传完成!",text.chat.id, text.message_id)
        bot.reply_to(text, "【"+okname+"】上传完成!")
        #os.remove(name)
        os.system('mv "'+name+'" /Bangumi')
        time.sleep(10)
        outte = os.system('python3 "/py/list.py"')
        outtt =os.system("python3 '/gu/Episode-ReName/EpisodeReName.py' '/onedrive/Bangumi'")
        outt3 =os.system("python3 '/gu/tgup/tgup.py' '"+str(okname)+"'")
        bot.reply_to(text, "【"+okname+"】所有操作完毕!😀")
        #bot.reply_to(text,outte)
    except Exception as err:
        bot.send_message("@Gu_Fan", err)
    #bot.send_message("@Gu_Fan", name)
    return name

#bot.send_message("@Gu_Fan", guup())
guup()
