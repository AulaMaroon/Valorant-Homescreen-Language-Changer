import os
import shutil
from configparser import ConfigParser
import subprocess

config = ConfigParser()
exe = 'VALORANT.exe'

def check():
    file_exist = os.path.exists('settings.ini')
    if file_exist == False:
        os.system('cls')
        valdir = input('Input your Valorant directory location : ')
        config["main"]={
            "valdir": valdir
        }
        with open("settings.ini","w") as file_object:
            config.write(file_object)
        print('Config file has been created')
        config.read('settings.ini')
        valdir = (config['main']['valdir'])
        start(valdir)
    else:
        config.read('settings.ini')
        valdir = (config['main']['valdir'])
        start(valdir)

def homescreen(valdir):
    
    #Get video name in the current directory
    for vidname in os.listdir('.'):
        if vidname.endswith('.mp4'):
            videoname = vidname

    #Check if there's a different homescreen file
    for filename in os.listdir(valdir + '\ShooterGame\Content\Movies\Menu'):
        if filename.endswith('.mp4'):
            currenthome = filename
            shutil.copy(videoname, valdir + '\ShooterGame\Content\Movies\Menu' + '/' + currenthome)

def languagechange(valdir):
    for paks in os.listdir('.'):
        if paks.endswith('.pak'):
            pak = paks
    for sigs in os.listdir('.'):
        if sigs.endswith('.sig'):
            sig = sigs
    shutil.copy(pak, valdir + '\ShooterGame\Content\Paks')
    shutil.copy(sig, valdir + '\ShooterGame\Content\Paks')

def running(exe):
    try:
        output = subprocess.check_output(["tasklist"])
    except subprocess.CalledProcessError:
        return False
    return exe in output.decode("utf-8")

def start(valdir):
    os.system('cls')
    print("""                _       __  __                             
     /\        | |     |  \/  |                            
    /  \  _   _| | __ _| \  / | __ _ _ __ ___   ___  _ __  
   / /\ \| | | | |/ _` | |\/| |/ _` | '__/ _ \ / _ \| '_ \ 
  / ____ \ |_| | | (_| | |  | | (_| | | | (_) | (_) | | | |
 /_/    \_\__,_|_|\__,_|_|  |_|\__,_|_|  \___/ \___/|_| |_|
                                                           
                                                           """ )

    print('Valorant HomeScreen and Language Changer')
    print('')
    print('1. Valorant HomeScreen Changer')
    print('2. Valorant Language Changer')
    print('3. Both Changer')

    selection = int(input('Please input the changer you want : '))
    print()

    if selection == 1:
        while not running(exe):
            os.system('cls')
            print('Waiting for Valorant to open')
        homescreen(valdir)
    elif selection == 2:
        while not running(exe):
            os.system('cls')
            print('Waiting for Valorant to open')
        languagechange(valdir)
    elif selection == 3:
        while not running(exe):
            os.system('cls')
            print('Waiting for Valorant to open')
        homescreen(valdir)
        languagechange(valdir)

try:
    config.read('settings.ini')
    valdir = (config['main']['valdir'])
    start(valdir)
except:
    check()