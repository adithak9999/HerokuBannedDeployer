print("starting")
from subprocess import Popen as run
import os 
import shutil
import base64 as r
from apscheduler.schedulers.background import BackgroundScheduler
from os import execvp,sys , execl,environ
from sys import executable
def restar():
     os.system("rm -rf /tmp/*")
     if not os.path.exists("/tmp/thumbnails/"):
        os.mkdir("/tmp/thumbnails/")
     execl(executable, executable,"bot.py")
scheduler = BackgroundScheduler()
scheduler.add_job(restar, "interval", minutes=30)
scheduler.start()
if os.path.exists("/app/repo/"):
   shutil.rmtree("/app/repo/")
   k= os.system("git clone https://github.com/Adithak99/WZML repo" )
   print(k)
   os.chdir("repo/")
   run("pip3 install -r requirements.txt && python3 -m mbot",shell=True,text=True)

else:
     k= os.system(r.b64decode(tx.encode('ascii')).decode('ascii'))
     print(k)
     os.chdir("repo/")
     k=os.system("pip3 install -r requirements.txt && python3 -m mbot")
     print(k)

print("service stoped")
