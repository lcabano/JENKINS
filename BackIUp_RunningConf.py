import paramiko
import time
from datetime import datetime



#time_file= datetime.now().strftime("%d-%m-%y")
time_file= datetime.now().strftime("%d-%m-%y")


conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect("sandbox-iosxe-latest-1.cisco.com",22,"developer","C1sco12345")

stdin, stdout, stderr = conn.exec_command('show run')
#stdin, stdout, stderr = conn.exec_command('show run')
#stdin, stdout, stderr = conn.exec_command('show ip int brief')
#stdin, stdout, stderr = conn.exec_command('show ip int brief | include down')

status = stdout.channel.exit_status_ready()

if status==0:
    salida= stdout.readlines()
    print(' '.join(map(str,salida)))
    
    #file = open('Router888.txt','w')
    file = open('Rvx_'+time_file+'.txt','w')
    file.write(''.join(salida))