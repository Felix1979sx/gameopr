#!/usr/bin/env python
#coding=utf-8

import os,sys,time
from prettytable import PrettyTable
from list_analysis import ListAnalysis

port = '22' #远程主机端口
dbuser = 'devuser'
dbpass = 'devuser'
listfile = '/home/game/scripts/list'

class getoutofloop(Exception):pass 

def showTable(file=listfile):
        os.system('tput clear')
        x = PrettyTable(["id","游戏大区","game","db"])
        x.align["id"] = "l"
        fd = open(file)
        for line in fd:
            x.add_row(line.split())
        print x

def jump():

    try:
    
        while True:
           
            os.system('tput clear')
            x = PrettyTable(["id","游戏大区","域名id","gameip","域名","dbip","dbport","dbname"])
            x.align["id"] = "l"
            fd = open(listfile)
            for line in fd:
                x.add_row(line.split())
            print x
        
            y = ListAnalysis(listfile)
            idlist = y.Server_Dic().keys()
        
            while True:
                input = raw_input("请输入需要跳转服务器的id  类型(game|db) <quit退出程序> ")   
                if input == 'quit':
                    raise getoutofloop()        
                else:
                    try:
                        id,ty = input.split()
                        if id in idlist:
                            if ty == 'game':
                                ip = y.Server_Dic()[id]['game_ip']
                                ret = os.system("ssh -p %s %s" % (port,ip))
                                if ret != 0:
                                    print "\033[1;31;40;5m 未正常跳转!! \033[0m"
                                    time.sleep(2)
                                    break
                                if ret == 0:
                                    break
                            elif ty == 'db':
                                ip = y.Server_Dic()[id]['db_ip']
                                dbport = y.Server_Dic()[id]['db_port']
                                dbname = y.Server_Dic()[id]['db_name']
                                ret = os.system("mysql -u%s -p%s -h%s -P%s %s " % (dbuser,dbpass,ip,dbport,dbname))
                                if ret != 0:
                                    print "\033[1;31;40;5m 未正常跳转!! \033[0m"
                                    time.sleep(2)
                                    break
                                if ret == 0:
                                    break
                        else:
                            print "\033[1;31;40;5m Id不存在，请重新输入 \033[0m"
                            continue
                    except:
                        print "\033[1;31;40;5m类型输入错误，重新输入 \033[0m"
        #continue    
    except getoutofloop:
        pass       
if __name__ == '__main__':
    jump() 