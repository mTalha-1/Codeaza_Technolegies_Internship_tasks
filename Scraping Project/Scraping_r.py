import grequests
from Extracting_Urls import extract_urls
from bs4 import BeautifulSoup
from lxml import etree

def get_urls():
    url = "https://www.laufen.co.at/produkte"
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"}
    request_site = grequests.get(url,headers=header)
    response_site = grequests.map([request_site])[0]
    return response_site

def extract_category_urls():
    soup = BeautifulSoup(get_urls().text, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    urls = []
    links = soup.find_all('a', class_ = 'cta-black')
    for link in links:
        # display the actual urls
        cat_link = 'https://www.laufen.co.at'+link.get('href')
        urls.append(cat_link)
    return urls

def extract_product_data(url):
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"}
    request_site = grequests.get(url,headers=header)
    response_site = grequests.map([request_site])[0]

    soup = BeautifulSoup(response_site.text, 'html5lib')
    prod_color = soup.find_all('input',class_="input-hidden nav-toggle")
    product_urls = []
    for p in prod_color:
        ur = p.get('href').split('e')[1]
        product_urls.append(url+ur)
    rq = (grequests.get(u) for u in product_urls)
    rs = grequests.map(rq)
    for r in rs:
        sp = BeautifulSoup(r.text,'html.parser')
        series = sp.find('h2', class_="coleccion-name").text
        name = sp.find('h1',class_="coleccion-title").text
        article_number = sp.find('p',class_="coleccion-article").split(':')[1]
        size = sp.find('span',id="dim-txt").split('mm')[0].split('x')
        length = size[0]
        width = size[1]
        height = size[2]
        colors_el = sp.find_all('span',class_="color-display")
        colors = [c.get_text(strip=True).split('-')[1] for c in colors_el]
        type_element = soup.find('select', class_='form-control cfg-option')
        selected_option = type_element.find('option', selected=True)
        Type = value = selected_option.get_text(strip=True)


        




if __name__ == "__main__":
    cat_urls = extract_category_urls()
    Products = extract_urls(cat_urls)
    for p in Products:
        extract_product_data(p)