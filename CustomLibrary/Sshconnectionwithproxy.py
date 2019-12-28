import subprocess
import openpyxl
import os
import paramiko
import socks
import datetime
import sys
import time
import calendar

reload(sys)
sys.setdefaultencoding('utf8')

ssh = ""
# sftp_client = none

def CL_Open_SSHConnection_With_Proxy(host, port, username, password, proxyHost, proxyPort):

    port = int(port)
    proxyPort = int(proxyPort)
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxyHost, proxyPort, False)
    paramiko.client.socket.socket = socks.socksocket
    SERVER_ENCODING = "utf-8"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=username, password=password)
    chan = ssh.invoke_shell()
    chan.settimeout(0)
    print "Server Connected"
    socks.setdefaultproxy()
    # ssh.close()
    return ssh
	
def CL_execute_comand(con, sshcmd):

    print "CL_execute_comand"
    print con
    stdin, stdout, stderr = con.exec_command(sshcmd)
    print 'executed'
    print stdout
    print stdin
    opt = stdout.readlines()
    opt = "".join(opt)
    return opt
	
def put_file(con, filename, data):

	sftp = con.open_sftp()
	#stdin, stdout, stderr = con.exec_command("cd /home/bscs1/bee/jobInput/massiveOCCGeneration")
	f = sftp.open(filename, 'w')
	f.write(data)
	f.close()
	con.close()
	

	


def CL_Close_Connection(ssh1):
    time.sleep(5)
    ssh1.close()

def Totaldays_month():
    now=datetime.datetime.now()
    return (calendar.monthrange(now.year, now.month)[1])
