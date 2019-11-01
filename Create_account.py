from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class redbull:

    def __init__(self):
        print('program begins')

    def create_account(self):
        driver= webdriver.Firefox()
        try:
            driver.get('http://www.fakemailgenerator.com/#/gustr.com')
            time.sleep(2)
            input_area = driver.find_element_by_xpath("//input[@id='home-email']")
            input_area.clear()
            input_area.send_keys(i + j + "")
            copy_button = driver.find_element_by_xpath("//button[@id='copy-button']")
            copy_button.click()
            time.sleep(1)
            driver.get("https://www.redbull.com/in-en/projects/red-bull-basement-university/project/1608")
            time.sleep(30)
            driver.find_element_by_xpath("//a[@class='rb-cookie-banner__btn']").click()
            time.sleep(1)
            for k in (1, 4):
                try:
                    login_button = driver.find_element_by_xpath(
                        "//div[@class='button button--red button__login display display--logged-out']")
                    time.sleep(1)
                except Exception:
                    continue

            login_button.click()
            time.sleep(8)
            button_email = driver.find_element_by_xpath("//button[@class='btn-text']")
            button_email.click()
            redbull_email = driver.find_element_by_xpath("//input[@id='email']")
            redbull_email.send_keys(i + j + "@gustr.com")
            button_continue = driver.find_element_by_xpath("//button[@type='submit']")
            button_continue.click()
            time.sleep(10)
            first_name = driver.find_element_by_xpath("//input[@id='firstName']")
            last_name = driver.find_element_by_xpath("//input[@id='lastName']")
            password = driver.find_element_by_xpath("//input[@id='password']")
            first_name.send_keys(i)
            last_name.send_keys(j)
            password.send_keys('wings')
            giughngub = driver.find_element_by_xpath("//button[@type='submit']")
            giughngub.click()
            time.sleep(10)
        except Exception:
            continue
        
        driver.close()




renn = redbull()
# renn.open_browser()
f_name = ['sheela', 'aastha']
l_name = ['kumawat', 'shethi']
for i,j in zip(f_name,l_name):
    renn.create_account()
    time.sleep(2)
