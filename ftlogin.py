from requests import post
from urllib import urlopen
from re import search
from time import sleep
d={	"magic":"key",				# magic key , unique to every login attempt
	"username":"YOUR_USER_NAME",		# USERNAME
	"password":"YOUR_PASSWORD"}		# PASSWORD

def site():
    try:					# try to open any website to open the firewall login page
        urlopen("http://aitpune.com").read()
    except:					# if fails , try again aafter 1.5 secs ( might fail due to internet issues
        sleep(1.5)
        site()

site()
try:
    a=urlopen("http://aitpune.com").read()		# copy HTML to 'a'
    d['magic']=search(r'name="magic" value="(.+)">',a).group(1)		# extract 'magic' key and store in dictionary
    post("http://aitpune.com/",data=d)				# send login form as POST with data in dictionary 'd'
    print "LOGGED IN SUCCESSFULLY"
except:
    print "FAILED"
    exit()
