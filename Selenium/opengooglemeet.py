from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

website = 'https://meet.google.com/#'
path = '/chromedriver'


service =   Service(executable_path =path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(website)
driver.set_page_load_timeout(10)

t = driver.find_element(by='xpath',value='//*[@id="page-content"]/section[2]/div/a')
driver.execute_script("arguments[0].scrollIntoView();",t)
sleep(3)
driver.implicitly_wait(3)
t1 = driver.find_element(by='xpath',value='//*[@id="page-content"]/section[1]/div/div[1]/h1')
driver.execute_script("arguments[0].scrollIntoView();",t1)
driver.implicitly_wait(3)
sleep(3)
setting = driver.find_element(by='xpath',value='//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/a/button')
setting.click()
sleep(5)