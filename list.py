import re
import os
import shutil
import telebot
from telebot import apihelper

bot = telebot.TeleBot("2052161417:AAECALXXXXXXXY34VCf2yd0VAd0", parse_mode=None)#推送消息用
apihelper.proxy = {'https':'socks5://127.0.0.1:8089'}

def fuzzyfinder(user_input, collection):
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

oklist = os.listdir("./onedrive/Bangumi")

dirlist = os.listdir("./onedrive/tmp")

def fil():
    for i in range(0,len(oklist)):
        listfil = fuzzyfinder(oklist[i], dirlist)
        if listfil != False:
            for b in range(0,len(listfil)):
                try:
                    text = bot.send_message("@Gu_Fan","开始分类【"+listfil[b]+"】到【"+oklist[i]+"】文件夹中")
                    shutil.move("./onedrive/tmp/"+listfil[b],"./onedrive/Bangumi/"+oklist[i]+"./Season 1")
                    bot.reply_to(text, "【"+listfil[b]+"】分类完成!")
                    #mvfillname = "/onedrive/tmp/"+listfil[b]
                    #okdir = "/onedrive/Bangumi/"+oklist[i]+"/Season 1"
                    #os.system('mv "'+name+'" /Bangumi')
                    #print("/onedrive/tmp/"+listfil[b]+"  转移成功")
                    return True
                except Exception as err:
                    bot.reply_to(text, "【"+listfil[b]+"】分类出错:"+str(err))
                    #print("/onedrive/tmp/"+listfil[b]+"  转移失败")
                    return False
zt = fil()
if zt == None:
    text = bot.send_message("@Gu_Fan","未找到需要分类的文件，可能需要手动分类。")
    txt_out = "文件列表:\n"
    for d in range(0,len(dirlist)):
        txt_out += str(d+1)+"."+str(dirlist[d])+"\n"
    bot.reply_to(text, str(txt_out))
#print("执行完成!")

#oklist = os.listdir("/onedrive/Bangumi")

