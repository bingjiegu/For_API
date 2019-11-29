from selenium import webdriver
import os, time, sys
from util import get_host
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
url = 'http://192.168.2.81:8515/#/login'
chromeOptions = webdriver.ChromeOptions()
# chrome 普通模式
chromedriver = PATH("../jihuo/chromedriver.exe")
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver, chrome_options=chromeOptions)


def isA(key, value):
    driver.get(url)
    time.sleep(2)
    try:
        location = driver.find_element_by_xpath("//*[contains(text(),'激活')]")
        if not location is None:
            location.click() 
            time.sleep(2)
            key_location = driver.find_element_by_xpath('/html/body/div/section/section/main/form/div[1]/div/div/input')
            if key_location.get_attribute('value') == key:
                driver.find_element_by_xpath('/html/body/div/section/section/main/form/div[2]/div/div/textarea').send_keys(value) 
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="bm-license-form"]/div[3]/div/button[1]/span').click()
                time.sleep(1)
                driver.close()
            else:
                print("请检查key值是否变化")
    except:
        print('激活过了，继续')
        driver.close()

