#mapIT.py
#python3
#Launches a map on the browser from command line or clipboard

import webbrowser,sys,pyperclip

if len(sys.argv) >1:
    #get address from the command line
    address = ''.join(sys.argv[1:])
else :
    #get address from clipboard
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
