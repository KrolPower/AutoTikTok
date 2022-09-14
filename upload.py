
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# open TikTokLogin.txt and get email and password info
# open text file in read mode
json_file = open("TikTokLogin.json")
 
# read whole file to a string
data = json.load(json_file)
 
# close file
json_file.close()

# set email and password variable
email = (data["info"][0]["email"])
password = (data["info"][0]["password"])


# Open Chrome
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)






# open tiktok
driver.get("https://www.tiktok.com/")



# click login button
time.sleep(1)
selectLogin = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/button')
selectLogin.click()

# click "Use phone / email / username"
time.sleep(1)
selectUseEmail = driver.find_element_by_xpath('//*[@id="loginContainer"]/div/div/a[2]/div')
selectUseEmail.click()

# click "login with email or username"
time.sleep(1)
selectLoginWithEmail = driver.find_element_by_xpath('//*[@id="loginContainer"]/div/form/div[2]/a')
selectLoginWithEmail.click()

# enter email
# selectEmail = driver.find_element_by_xpath('//*[@id="loginContainer"]/div/form/div[1]/input')
# selectEmail.send_keys(email)
print("\n" + bcolors.OKGREEN + str(email) + bcolors.ENDC)

# enter username
# selectPassword = driver.find_element_by_xpath('//*[@id="loginContainer"]/div/form/div[2]/div/input')
# selectPassword.send_keys(password)
print("\n" + bcolors.OKGREEN + str(password) + bcolors.ENDC)


# need to manually click "Log In"
# selectLoginButton = driver.find_element_by_xpath('//*[@id="loginContainer"]/div/form/button')
# selectLoginButton.click()
print("\n" + bcolors.OKGREEN + str("------------------------------ Click Log In Button ------------------------------") + bcolors.ENDC)
time.sleep(5)
print("------- Waiting -------")
time.sleep(10)
print("------- Proceding With Upload -------")


# click "upload"
time.sleep(30)
print(bcolors.OKGREEN + "Calling Upload now" + bcolors.ENDC)
upload = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/a/div/span')
upload.click()
time.sleep(30)


# select file
selectFile = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/button')

# get file path
file_path = "Output\Piper\Piper_0.mp4"

# upload file
driver.sendKeys(file_path)



# # wait for Post Button text

# from datetime import datetime
# from selenium.webdriver.support.ui import WebDriverWait

# WebDriverClock = datetime.now()
# current_time_webdriver = WebDriverClock.strftime("%H:%M:%S")
# print("\nTime before waiting for CLICK ME button with webdriver=", current_time_webdriver)
# WebDriverWait(driver, 10).until(driver.presence_of_element_located((driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/button/div'))))
# ButtonFound = datetime.now()
# current_time_ButtonFound = ButtonFound.strftime("%H:%M:%S")


# print("Time when Button Found=", current_time_ButtonFound)

        



# # click post button
# selectPost = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[7]/div[2]/button')




# # Close Chrome
# driver.quit()
time.sleep(1000)

