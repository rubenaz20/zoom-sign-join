## Code to Automatically open Zoom program to join a meeting and record meeting is required

#####################################

## Please read through the read me to understand how this works to implement it for your set up

#####################################

## You need the pyautogui library, best way to install is using 'pip install pyautogui'
## in essence this script uses your keyboard and mouse to automatically open zoom from start menu and click and enter meeting id
## some settings of zoom itself needs to be changed for this script to work correctly

## documentation for pyautogui

########################################################

## https://pyautogui.readthedocs.io/en/latest/index.html

########################################################

# importing libraries
import pyautogui 
import time

#####   Joining Zoom Meeting   ###################

#######################################################################################
#Enter the meeting id as a string here *important that it is in string format
meet_id = '123456789'

#esc clicked to ensure that the win key will open up correctly in the next step
pyautogui.press('esc',interval=0.1)

time.sleep(0.2)

#these lines are simulating starting up zoom by pressing windows key and typing zoom to open program
pyautogui.press('win',interval=0.1)
pyautogui.write('zoom')
pyautogui.press('enter',interval=0.5)


#time delay to factor for zoom app to load up, good buffer is like 10 sec but its case specific
time.sleep(10)


#####   SignIn into Zoom   ###################

user = '123456789'
user_pwd = '123456789'

# Check is loggedIn and signout
loggedIn = pyautogui.locateOnScreen('loggedIn.png')

if loggedIn {
  # Click on greenBullet
  greenBullet = pyautogui.locateOnScreen('loggedIn_green_bullet.png')
  center_greenBullet = pyautogui.center(greenBullet)
  pyautogui.click(center_greenBullet)
  
  # Click on signout
  logOut = pyautogui.locateOnScreen('logOut.png')
  center_logOut = pyautogui.center(logOut)
  pyautogui.click(center_logOut)
  
  time.sleep(4)
}

# Search user field by placeholder
user_box = pyautogui.locateOnScreen('username_placeholder.png')
center_username = pyautogui.center(user_box)
pyautogui.click(center_username)
pyautogui.typewrite(user)

# Search user pwd field by placeholder
pwd_box = pyautogui.locateOnScreen('user_pwd_placeholder.png')
center_pwd = pyautogui.center(pwd_box)
pyautogui.click(center_pwd)
pyautogui.typewrite(user_pwd)

# Search signin button
signinButton = pyautogui.locateOnScreen('signinButton.png')
center_signinButton = pyautogui.center(signinButton)
pyautogui.click(center_signinButton)

time.sleep(8)


#this part simulates clicking join meeting, entering meeting id and pressing enter to join
##Make sure the joinButton.png file is located in the same folder as the python file or else it will not work
##this tells the script where to click to join the meeting

x,y = pyautogui.locateCenterOnScreen('joinButton.png')
pyautogui.click(x,y)


pyautogui.press('enter',interval=1)
## the interval of 1 second is important, if not there, then the meeting id will not be inputted
pyautogui.write(meet_id)
pyautogui.press('enter',interval=1)


###### password OPTIONAL!!! #####
# if your meeting has a password then uncomment the code below and enter it here


# change the value of the variable to your password
password = 'password'

#time.sleep(3)
#pyautogui.press('enter',interval=1)
#pyautogui.write(password)
#pyautogui.press('enter',interval = 1)
##### IF YOUR MEETING HAS NO PASSWORD PLEASE LEAVE THIS SECTION AS IS AND DONT UNCOMMENT
