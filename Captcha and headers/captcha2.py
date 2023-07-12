from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

try:
    service =   Service(executable_path = "/chromedriver")
    driver = webdriver.Chrome(service=service)
except Exception as e:
    print(e)
else:
    driver.maximize_window()

website = "https://www.google.com/recaptcha/api2/demo"
try:
    driver.set_page_load_timeout(100)
    driver.implicitly_wait(50)
    driver.get(website)
except Exception as e:
    print(e)


driver.implicitly_wait(30)
frame_xpath = '//*[@id="recaptcha-demo"]/div/div/iframe'
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frame_xpath)))

checkbox_xpath = '//*[@id="recaptcha-anchor"]'
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath))).click()
input()
