from requests import post
from urllib import urlopen
from re import search
from time import sleep
d={	"magic":"key",
	"username":"YOUR_USER_NAME",
	"password":"YOUR_PASSWORD"}

def site():
    try:
        urlopen("http://aitpune.com").read()
    except:
        sleep(1.5)
        site()

site()
try:
    a=urlopen("http://aitpune.com").read()
    d['magic']=search(r'name="magic" value="(.+)">',a).group(1)
    post("http://aitpune.com/",data=d)
    print "LOGGED IN SUCCESSFULLY"
except:
    print "FAILED"
    exit()
