# ftlogin
program to automatically login to fortinet on startup
1) Copy the "ftlogin.py" file in your HOME directory ( /home )
   -open file in any texteditor ( eg gedit)
   -replace YOUR_USER_NAME and YOUR_PASSWORD(line no. 6 & 7)with your fortinet username and password and SAVE
2) Press "Start/Windows" button , search for the application "STARTUP APPLICATIONS"
3) Click on "ADD"
4) NAME : anything you want
   COMMAND : python ftlogin.py
   COMMENT : not needed
DONE !
