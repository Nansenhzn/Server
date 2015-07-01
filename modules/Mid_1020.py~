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
		if self.sys_command =='ping':
		        status,self.Runresult=commands.getstatusoutput('ping '+self.hosts+' -c 3')
		elif self.sys_command =='top':
			str1='top -n 1 |grep Cpu |sed \'s/.*(s) ://g \'|cut -d ,  -f 4|cut -d % -f 1|cut -d \' \' -f 2'
			status,self.Runresult=commands.getstatusoutput(str1)
		elif self.sys_command =='mem':
			#str2 = 'grep MemTotal /proc/meminfo'
			#status,self.Runresult=commands.getstatusoutput(str2)
			s1=commands.getoutput('grep MemFree /proc/meminfo')
			status=commands.getstatus('grep MemFree /proc/meminfo')
			s2=commands.getoutput('grep MemTotal /proc/meminfo')
			s2=s2.split('MemTotal:')[1].split(' kB')			
			s1=s1.split('MemFree:')[1].split(' kB')
			s = float(s1[0])/float(s2[0])
			self.Runresult=str(s)
			#self.Runresult=s2[0]+","+s1[0]
			#self.Runresult=s2.strip('metoalkb')
		elif self.sys_command =='network':
			#str1='top -n 1 |grep Cpu |sed \'s/.*(s) ://g \'|cut -d ,  -f 4|cut -d % -f 1|cut -d \' \' -f 2'
			#str1='cat /proc/stat'
			str1='ifconfig eth0 |grep \'接收字节\''
			status,self.Runresult=commands.getstatusoutput(str1)
		else:
                	status,self.Runresult=commands.getstatusoutput(self.sys_command)
        except Exception,e:
		print str(e)
		return str(e)
        return self.Runresult
