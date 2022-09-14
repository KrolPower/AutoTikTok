
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time

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







# # Close Chrome
# driver.quit()
time.sleep(10)

