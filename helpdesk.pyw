import os
import subprocess
import time
import sys
import pickle
import webbrowser
import pystray

from PIL import Image

#if the save directory doesn't exist, create it
appDataDir = os.popen("echo %appdata%"+'/helpdesk').read().replace("\n", "")

if not os.path.exists(appDataDir):
    os.makedirs(appDataDir)

def openHelpdesk():
    #get environment details
    domain = os.popen("echo %USERDOMAIN%").read()
    hostname = os.popen("hostname").read()
    username = os.popen("echo %USERNAME%").read()
    
    if os.path.isfile(appDataDir + "/contacts.p") :
        contacts= pickle.load(open(appDataDir + "/contacts.p", "rb"))
        if username in contacts:
             #format the url
            url = 'http://starfruitsolutions.com/support?' + 'domain=' + domain + '&hostname=' + hostname + '&username=' +username + "&email=" + contacts[username]['email'] + "&phone=" + contacts[username]["phone"]

            webbrowser.open_new(url)
        else:
            changeContactInfo()
            openHelpdesk()
    else:
        changeContactInfo()
        openHelpdesk()
    

def changeContactInfo():
    contactProcess = subprocess.Popen(['contact.exe'])
    contactProcess.wait()


def exitTray(icon):
    icon.visible = False  # Need it to stop the main while loop. I think any global var also will do the thing
    icon.stop()  # Stop icon thread (?)

def setup(icon):
    icon.visible = True
    
    while icon.visible:
        # Some payload code        
        
        time.sleep(5)
        
def initIcon():
    #initialize
    icon= pystray.Icon('Starfruit Solutions -Helpdesk')
    icon.title= 'Starfruit Solutions -Helpdesk'
    icon.icon = Image.open("helpdesk.ico")
    
    #menu items
    menu_openHelpdesk= pystray.MenuItem('Submit a Ticket',openHelpdesk, default=True)
    menu_updateContactInfo= pystray.MenuItem('Update Contact Info', changeContactInfo)
    menu_close= pystray.MenuItem('Close', lambda : exitTray(icon))

    #menu
    icon.menu= pystray.Menu(menu_openHelpdesk, menu_updateContactInfo, menu_close)

    #start    
    icon.run(setup)

#start
initIcon()
    