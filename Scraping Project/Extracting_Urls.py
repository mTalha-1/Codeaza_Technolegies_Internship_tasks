from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import logging

logging.basicConfig(filename='log_file.txt', filemode='w',level=logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s - %(lineno)d')

'''This function is for connecting webdriver of your browser. 
You have to first instsall webdriver in your system.
If your webdriver is in another path, you can change executable path in funtion.
'''
def webdriver_connection():
    try:
        service =   Service(executable_path = "/chromedriver")
        driver = webdriver.Chrome(service=service)
    except Exception as e:
        logging.critical(e)
    else:
        driver.maximize_window()
        return driver

def opening_url(web_url,driver):
    website = web_url
    try:
        driver.set_page_load_timeout(100)
        driver.implicitly_wait(50)
        driver.get(website)
    except Exception as e:
        logging.error(e)

def find_element_urls(driver,el_xpath):
    try:
        url = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH,el_xpath))
        )
    except NoSuchElementException as e:
        logging.error(e)
        return ''
    else:
        return url

#This function is taking list of urls of each category and then return total products urls from each category.
def extract_urls(category_urls):
    prod_url = []
    for cat_url in category_urls:
        driver = webdriver_connection()
        opening_url(cat_url,driver)
        no_of_prod_xpath = '/html/body/div[1]/section/div/div/div/div/div[6]/section/div/div[2]/div/section[3]/div[1]/div[5]/div/div/a/span[2]'
        no_of_product_el = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,no_of_prod_xpath))
        )
        if no_of_product_el.text == '':
            no_of_pages = 0
        else:
            no_of_pages = int(int(no_of_product_el.text.split(" ")[6])/12)

        print("Scraping urls of "+cat_url.split('/')[-1])
        print("______________________________")

        prod_xpath = '//div [@class="col-6 col-md-6 col-lg-3 mb-3 m-2-col"]'
        i = 0
        while i <= no_of_pages:
            print("Scraping page ",i)
            if i == 0:
                page_url = "https://www.laufen.co.at/produkte/"+cat_url.split('/')[-1]
            else:
                page_url = "https://www.laufen.co.at/produkte/"+cat_url.split('/')[-1]+"?page="+str(i)
            
            opening_url(page_url,driver)
            urls = find_element_urls(driver,prod_xpath)
            for u in urls:
                prod_url.append('https://www.laufen.co.at'+u.get_attribute('data-url'))
            i +=1
    return list(set(prod_url))

if __name__ == "__main__":
    url = ["https://www.laufen.co.at/produkte/dusch-wcs"]
    urlp = extract_urls(url)
    print(urlp)
    print(len(urlp))