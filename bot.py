from os import system,chdir
from base64 import b64decode
from subprocess import Popen as run
repo = "Z2l0IGNsb25lIGh0dHBzOi8vZ2l0aHViLmNvbS9BZGl0aGFrOTkvV1pNTCBib3Q="
system(b64decode(repo).decode('ascii'))

system("git clone https://github.com/Adithak99/WZML bot")
chdir("bot/")
run("pip3 install -r requirements.txt && python3 -m bot",shell=True,text=True)
print("Service Stopped")
