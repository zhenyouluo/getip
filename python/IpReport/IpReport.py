#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket
import time
import json
import uuid
import sys

DEF_HOST ="mtzijin.com"
DEF_PORT =19601
DEF_UUID =str(uuid.uuid1())

uid =DEF_UUID
host =DEF_HOST
port =DEF_PORT
report_timer_sec =4

# 获取本机内网ip
def GetLocalIp():
    sn ='NULL'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('www.baidu.com', 80))
        sn =s.getsockname()
        s.close()
    except Exception as e:
        print e
    finally:
        s.close()
    return str(sn)

def IpReport(s):
    global uid
    
    d ={"localip":GetLocalIp()}
    while True:
    
        # 读取配置信息
        ff =None 
        try:
            uid =DEF_UUID
            host =DEF_HOST
            port =DEF_PORT
            
            ff = open('C:/IpReport.txt')
            all = ff.read()
            conf =json.loads(all)
            if conf.has_key('uid') and len(conf['uid'])>0 :
                uid =conf['uid']
            if conf.has_key('host') and len(conf['host'])>0 :
                host =conf['host']
            if conf.has_key('port') and len(conf['port'])>0 :
                port =int(conf['port'])
        except Exception,e :
            print e
        finally:
            if ff:
                ff.close()

        # 序列化并发送
        encodedjson = json.dumps({uid: d}) 
        print 'host=',host,' port=',port,' encodedjson=',encodedjson
        s.sendto(encodedjson, (host, port) )
        
        time.sleep(report_timer_sec)

def Run(conf_file):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            IpReport(s)
        except Exception as e:
            print e
        finally:
            s.close()
        time.sleep(4)
        continue

if __name__=="__main__":
    conf_file =''
    if len(sys.argv)>1:
        conf_file =sys.argv[1]
    Run(conf_file)

