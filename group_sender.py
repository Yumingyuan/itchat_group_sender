﻿# -*-coding:utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   
import itchat
from itchat.content import TEXT
from itchat.content import *
import time
import os
def send_to_all_group():
	rooms=itchat.get_chatrooms(update=True)
	if rooms is not None:
		for room in rooms:
			try:
				message_need_send="To \"%s\" 的朋友们 "%room['NickName'].encode("utf-8",'ignore')+"祝福语"
				print u'消息已发送至:',room['NickName'].encode("GBK",'ignore')
				itchat.send(u'%s'%message_need_send,room['UserName'])
			except UnicodeEncodeError:
				pass
	else:
		print 'Error:No chat room to send!'
if __name__=='__main__':
  itchat.auto_login()
  send_to_all_group()
