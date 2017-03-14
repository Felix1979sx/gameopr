#!/usr/bin/env python
#coding=utf-8
import sys

class ListAnalysis(object):
    version = 1.0
    "the script for youxigu game host list analysis"

    def __init__(self,listfile):
        self.listfile = listfile

    def Server_List(self,id,n=2):
    
        """
        input the game id, eg '1 2' ,output the game ip list xxx.xxx.xx.xxx  xxx.xxx.xxx.xxx
        if input all ,then output all the game ip list;if u need dblist ,then n = 4
        """
    
        fd = open(self.listfile)
        gamedic = {}
        for line in fd:
            vars = line.split()
            gamedic[vars[0]] = vars[n]
        fd.close()

        iplist=[]
        if id != 'all':
            for id in id.split(','):
                if id in gamedic:
                    iplist.append(gamedic[id])
                else:
                    print "包含错误的id号"
            return iplist
        if  id == 'all':
            iplist=gamedic.values()
            return iplist    

    def Server_Dic(self):
        '''
        
         output server dic 。 eg {id：{id_name:'广东一区', gameip：'xx.xx.xx.xx',dbip:'xx.xx.xx.xx',dbport:'xxx',dbname:'dbname'},
                                  id: {id_name:'xxxxxxxx', gameip: 'xx.xx.xx.xx',dbip:'xx.xx.xx.xx',dbport:'xxx',dbname:'dbname'}
                                 }
        '''
        
        
        fd = open(self.listfile)
        sv_dic = {}
        for line in fd:
            vars = line.split()
            id = vars[0]
            sv_dic[id] = {}
            sv_dic[id]['id_name'] = vars[1]
            sv_dic[id]['game_ip'] = vars[2]
            sv_dic[id]['db_ip'] = vars[3]
#            sv_dic[id]['db_port'] = vars[4]
#            sv_dic[id]['db_name'] = vars[5]
        return sv_dic

    def Server_Tuple(self):
        '''
        output server named tuple: eg(Zone(id=1,id_name='广东一区',gameip='x.x.x.x',dbip='x.x.x.x',dbport='3306',dbname='dbname'),
                                      Zone(id=2,id_name='xxxxxxxx',gameip='x.x.x.x',dbip='x.x.x.x',dbport='xxxx',dbname='xxxx')
                                             )
        
        '''
        import collections
        sv_tp = collections.namedtuple('Zone', 'id,id_name,gameip,dbip,dbport,dbname')
        sv_tuple = []
        fd = open(self.listfile)
        for line in fd:
            vars = line.split()
            sv_list.append(Zone("vars[0], vars[1], vars[3], vars[5], vars[6],vars[7]"))
        return sv_tuple

    def Convert_Ip(self,ip,n=3):
        fd = open(self.listfile)
        for line in fd:
            if ip == line.split()[n]:
                return line.split()[1]
    def Convert_Id(self,ip,n=3):
        fd = open(self.listfile)
        for line in fd:
            if ip == line.split()[n]:
                return line.split()[0]
