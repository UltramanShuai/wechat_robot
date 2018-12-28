# _*_coding:utf-8_*_
# Author   : Leo
# Time     : 23/12/2018
import os
import shutil

import itchat
from itchat.content import TEXT, PICTURE
import pic


who_send = None

last = None


@itchat.msg_register(PICTURE, isFriendChat=True)
def pic_reply(msg):
    global who_send
    msg['Text'](msg['FileName'])
    who_send = msg['FromUserName']
    if who_send != itchat.search_friends(name='Leo')[0]['UserName']:
        if msg['FileName'].split(".")[1] == "gif":
            itchat.send("[Auto reply]I can't transform this type picture!", toUserName=who_send)
        else:
            try:
                itchat.send("[Auto reply]please wait：￥%……&……#*", toUserName=who_send)
                return_name = pic.zip_pic(msg['FileName'])
                itchat.send('@img@%s' % return_name, toUserName=who_send)
                itchat.send("[Auto reply]Here you are! You are welcome 0.0 ", toUserName=who_send)
                os.remove(return_name)
            except:
                itchat.send("[Auto reply]Error！", toUserName=who_send)

    friend_path = "./picture/" + msg['FromUserName'] + "/"
    if not os.path.isdir(friend_path):
        os.makedirs(friend_path)
    new_path = friend_path + msg['FileName']
    shutil.move(msg['FileName'], new_path)


itchat.auto_login()
itchat.run()
