import os
import json

gugu = os.listdir("/onedrive/Bangumi")
gugu1 = os.listdir("./dm-list")
for i in range(0,len(gugu)):
    jsoninp = {
        'name':gugu[i],
        'dirul':""
    }
    inlist = open("./dm-list/"+str(i)+".json","w")
    inlist.write(str(jsoninp))
    inlist.close()

for i in range(0,len(gugu1)):
    inlist = open("./dm-list/"+str(gugu1[i]),"rb")
    red_json = str(inlist.read())
    print(red_json["name"])
    inlist.close()