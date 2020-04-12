from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pynput.keyboard import Key, Controller

#Your instagram username
username=""
#Your instagram password
password=""
photoName="" #Photo must be placed in the user directory

#Mobile emulation needed for story uploads
mobile_emulation = { "deviceName": "Pixel 2" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

#Start up driver
driver = webdriver.Chrome('/Users/ashmin/Downloads/chromedriver', desired_capabilities=chrome_options.to_capabilities())

#Get login page
driver.get('http://instagram.com/accounts/login')
time.sleep(3)

#Insert username
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[4]/div/label/input").send_keys(username)
time.sleep(1)

#Insert password
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[5]/div/label/input").send_keys(password)
time.sleep(1)

#Click login
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[7]/button/div").click()
time.sleep(5)

#Click not now
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/button").click()
time.sleep(2)

#Click cancel
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
time.sleep(0.5)

#Click add story
driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[1]/div/div/div/div[1]/button").click()
time.sleep(0.5)

#Click not now again
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[5]/button").click()

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

driver.find_element_by_xpath("//*[@id='react-root']/section/footer/div/div/button").click()
