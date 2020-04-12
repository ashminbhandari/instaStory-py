from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pickle #Cookie dumps
from pynput.keyboard import Key, Controller

def executeElement(xPath, sleepTime, keys):
    try:
        if(keys != '0'):
            driver.find_element_by_xpath(xPath).send_keys(keys)
        else:
            driver.find_element_by_xpath(xPath).click()
        time.sleep(sleepTime)
    except NoSuchElementException:
        print("Couldn't find an element")

#Your instagram username
username=""
password=""
photoName="IMG" #Photo must be placed in the user directory

#Mobile emulation needed for story uploads
mobile_emulation = { "deviceName": "Pixel 2" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

#Start up driver
driver = webdriver.Chrome('/Users/ashmin/Downloads/chromedriver', desired_capabilities=chrome_options.to_capabilities())

#Get login page
driver.get('http://instagram.com/accounts/login')
time.sleep(3)

#Insert username
executeElement("//*[@id='react-root']/section/main/article/div/div/div/form/div[4]/div/label/input", 1, username)

#Insert password
executeElement("//*[@id='react-root']/section/main/article/div/div/div/form/div[5]/div/label/input", 1, password)

#Click login
executeElement("//*[@id='react-root']/section/main/article/div/div/div/form/div[7]/button/div", 5, '0')

#Click save info
executeElement("//*[@id='react-root']/section/main/div/div/section/div/button", 5, '0')

#Click cancel
executeElement("/html/body/div[4]/div/div/div[3]/button[2]", 5, '0')

#Click add story
executeElement("//*[@id='react-root']/section/nav[1]/div/div/header/div/div[1]/button", 1, '0')

#Click not now again
executeElement("/html/body/div[4]/div/div[2]/div/div[5]/button", 1, '0')

#Activate keyboard
keyboard = Controller()

#Write down the file name
for char in photoName:
    keyboard.press(char)
    keyboard.release(char)

keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(1)

#Open inspect element, this shortcut will change for windows
keyboard.press(Key.cmd)
keyboard.press(Key.shift)
keyboard.press('c')
keyboard.release('c')
time.sleep(2)

keyboard.press('c')
time.sleep(2)

#Toggle device mode, this shortcut will change for windows
keyboard.press('M')
keyboard.release('M')
keyboard.release(Key.cmd)
keyboard.release(Key.shift)
time.sleep(1)

executeElement("//*[@id='react-root']/section/footer/div/div/button", 10, '0')

driver.close()









