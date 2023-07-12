from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Set Chrome driver path
chrome_driver_path = "C:\\Utility\\BrowserDrivers\\chromedriver.exe"

# Configure Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
userdatadir = 'C:/Users/dell/AppData/Local/Google/Chrome/User Data'
chrome_options.add_argument("profile-directory=Default")
chrome_options.add_argument(f"--user-data-dir={userdatadir}")
# chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
# chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("disable-infobars")
# chrome_options.add_argument("--disable-extensions")

# Create a Chrome driver instance
service =   Service(executable_path = "/chromedriver")
driver = webdriver.Chrome(options=chrome_options,service=service)

# Open the webpage
driver.get("https://rsps100.com/vote/760")
driver.implicitly_wait(100)
# Switch to the reCAPTCHA iframe
frame_xpath = "//iframe[starts-with(@name, 'a-') and starts-with(@src, 'https://www.google.com/recaptcha')]"
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frame_xpath)))

# Click on the reCAPTCHA checkbox
checkbox_css_selector = "div.recaptcha-checkbox-checkmark"
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, checkbox_css_selector))).click()

# Close the browser
driver.quit()

# from selenium.common.exceptions import NoSuchElementException
# from time import sleep
# chrome_options = webdriver.ChromeOptions()

# chrome_options.add_experimental_option("useAutomationExtension", False)

# chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])






