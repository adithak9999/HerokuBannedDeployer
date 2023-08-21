print("starting")
from subprocess import Popen as run
import os 
import shutil
import base64 as r
#from apscheduler.schedulers.background import BackgroundScheduler
from os import execvp,sys , execl,environ
from sys import executable
if os.path.exists("/app/repo/"):
   shutil.rmtree("/app/repo/")
   k= os.system("git clone https://github.com/Adithak99/WZML repo" )
   print(k)
   os.chdir("repo/")
   run("pip3 install -r requirements.txt && python3 -m mbot",shell=True,text=True)

else:
     k= os.system("git clone https://github.com/Adithak99/WZML repo")
     print(k)
     os.chdir("repo/")
     k=os.system("pip3 install -r requirements.txt && python3 -m bot")
     print(k)

print("service stoped")
