import os
import subprocess
import sys


#// this is hydra Tool built for more simplified and easy to use attack

print ('Hello! Welcome to Attack ME\n'
'This tool is created for simplified attacks using Hydra :D\n'
'Please use Hydra-THC cli commands!\n\n')

#// Main Commands and controls

server=input('target server:')
protocol=input('target protocol used:')
ports=input('Any Specific Port to use:')
username=input('username:')
password=input('Passowrd:wordlist(-p/-P) specify using command:')
invalid=input('What is your targets invalid user:Pass?none leave blank:')
commands=input('Any Other Additional commands:')
proxy=input('Proxy:')
save=input('Save filename:')

print('\n\n')
#// Review command line before proceeding
confirm=print((server),(protocol),(ports),(username),(password),(invalid),(commands),(proxy))
print('\n\n')


#//make things easy please:
def call():
    tint=subprocess.call(["Hydra",(server),(protocol),"-s"(ports),"-l"(username),(password),(invalid),(commands)(proxy),"-o"(save)])
    subprocess.call(["Clear"])
    subprocess.call(["python attackme.py"])
    print(tint)
    return 0;
#// Database
database=['Asterisk', 'AFP', 'Cisco AAA', 'Cisco auth','Cisco enable','CVS','Firebird','FTP',
 'HTTP-FORM-GET', 'HTTP-FORM-POST', 'HTTP-GET','HTTP-HEAD','HTTP-POST','HTTP-PROXY',
 'HTTPS-FORM-GET', 'HTTPS-FORM-POST','HTTPS-GET', 'HTTPS-HEAD', 'HTTPS-POST',
 'HTTP-Proxy', 'ICQ', 'IMAP','IRC', 'LDAP', 'MS-SQL', 'MYSQL', 'NCP', 'NNTP', 'Oracle Listener',
 'Oracle SID','Oracle', 'PC-Anywhere','PCNFS','POP3','POSTGRES','RDP','Rexec','Rlogin',
 'Rsh', 'RTSP', 'SAP/R3', 'SIP', 'SMB', 'SMTP', 'SMTP Enum', 'SNMP', 'SOCKS5',
 'SSH', 'SSHKEY', 'Subversion', 'Teamspeak', 'Telnet', 'VMware-Auth',
 'VNC','XMPP']
#// Results area..
if confirm == protocol == database:
    call()
else:
    print('wrong protocol or something! goto github for help!\n')
    subprocess.call(['clear'])
    subprocess.call(['python attackme.py'])
