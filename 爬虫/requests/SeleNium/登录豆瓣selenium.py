import requests
from selenium import webdriver
import time
from yundama import discern

driver = webdriver.Chrome('../chromedriver')

driver.get('https://www.douban.com/')
time.sleep(3)

driver.find_element_by_name('form_email').send_keys('13523077502')
driver.find_element_by_name('form_password').send_keys('weiai390621')
time.sleep(3)

#获取图片
valicode_url = driver.find_element_by_id("captcha_image").get_attribute("src")
resp = requests.get(valicode_url)
file_path = "captcha_image.jpeg"
with open(file_path, "wb") as file:
    file.write(resp.content)

#调用云打码
valicode = discern(filepath=file_path,codetype=3000)

#输入验证码
driver.find_element_by_name("captcha-solution").send_keys(valicode)

# 等待
time.sleep(2)

driver.find_element_by_class_name('bn-submit').click()