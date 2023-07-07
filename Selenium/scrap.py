from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

website = 'https://www.coursera.org/search?query=data%20analytics&'
path = '/chromedriver'


service =   Service(executable_path =path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(website)
driver.set_page_load_timeout(10)

title = driver.find_element(by='xpath',value="//h2[@class='cds-119 css-h1jogs cds-121']")
print(title.text)

titles = driver.find_elements(by='xpath',value="//h2[@class='cds-119 css-h1jogs cds-121']")
for t in titles:
    print(t.text)

for t in titles:
    driver.execute_script("arguments[0].scrollIntoView();",t)
    sleep(2)


driver.get('https://www.coursera.org/')

driver.set_page_load_timeout(20)

search = driver.find_element(by='xpath',value="//input[@class='react-autosuggest__input']")
search.send_keys("Data Science")

search_button = driver.find_element(by='xpath',value='//*[@id="rendered-content"]/div/header/div/div/div[2]/div[1]/div[3]/div/form/div/div/div[1]/button[2]/div')
search_button.click()
input()
driver.quit()


