# -*- coding: utf-8 -*-
import commands
class Modulehandle():
    def __init__(self,moduleid,hosts,sys_command):
        self.Runresult = ""
        self.moduleid = moduleid
        self.sys_command= sys_command
        self.hosts = hosts


    def run(self):
        try:
	    print self.hosts
	    if self.sys_command =='ping':
	        status,self.Runresult=commands.getstatusoutput('ping '+self.hosts+' -c 4')
        except Exception,e:
            print str(e)
            return str(e)
        return self.Runresult
