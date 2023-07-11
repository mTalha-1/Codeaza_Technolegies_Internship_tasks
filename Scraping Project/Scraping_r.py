import grequests
from Extracting_Urls import extract_urls
from bs4 import BeautifulSoup
import csv


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

Data = []
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
        #Product_Series
        series = sp.find('h2', class_="coleccion-name").text
        #Product_name
        name = sp.find('h1',class_="coleccion-title").text
        #Product_article_number
        article_number = sp.find('p',class_="coleccion-article").text.split(':')[1]
        #Product L,W,H
        size = sp.find('span',id="dim-txt").text.split('mm')[0].split('x')
        length = size[0]
        width = size[1]
        height = size[2]
        #Products colors
        colors_el = sp.find_all('span',class_="color-display")
        colors = [c.get_text(strip=True).split('-')[1] for c in colors_el]
        #Product Type
        # type_element = soup.find('select', class_='form-control cfg-option')
        # selected_option = type_element.find('option', selected=True)
        # Type = value = selected_option.get_text(strip=True)
        #Product Main Image
        try:
            main_image_find = sp.find_all('img',{'data-finish':"n-finished-"+str(article_number)})[0]
        except Exception as e:
            main_image = ''
        else:
            main_image = "https://www.laufen.co.at"+main_image_find.get('src')
        #Product Sub Image
        try:
            div_tags = sp.find_all('div', class_='slick-option-all')
        except Exception as e:
            sub_images = ''
        else:
            sub_images = []
            for div_tag in div_tags:
                # Find the <img> tag within the current <div> tag
                img_tag = div_tag.find('img')
                # Extract the src attribute value
                src_value = img_tag['src']
                sub_images.append(src_value)
        
        #Product_Long_Description
        try:
            long_description = sp.find('p', class_="clamp").text
        except Exception as e:
            long_description = ""
        #Product Short_Description
        div_tags = sp.find_all('div', class_='row r-body zero-margin-bottom')
        description = ''
        for div_tag in div_tags:
            p_tags = div_tag.find_all('p')
            for p_tag in p_tags:
                text = p_tag.text.strip()
                description = description+"\n"+text

        #Products_Maintanance Sheet
        matching_link = sp.find_all('img', class_="image-installation-maintenance")
        DataSheet_link = []
        for l in matching_link:
            if l.get('alt') == 'Technisches Datenblatt':
                DataSheet_link.append(l.get('src'))
            else:
                DataSheet_link = ''

        Product_Data = {'Series':series,'Name':name,'Article_number':article_number,'Length':length,'Width':width,'Height':height,'Colors':[colors],'Main_image':main_image,'Sub_images':[sub_images],'Long_description':long_description,'Description':description,'DataSheet_links':[DataSheet_link]}
        Data.append(Product_Data)
        print('good')
        

if __name__ == "__main__":

    cat_urls = extract_category_urls()
    Products = extract_urls(cat_urls=cat_urls[:3])
    for URL in Products:
        extract_product_data(URL)
    

    Header = ['Series','Name','Article_number','Length','Width','Height','Colors','Main_image','Sub_images','Long_description','Description','DataSheet_links']

    with open('data.csv','w') as file:
        writer = csv.DictWriter(file,fieldnames=Header)
        writer.writeheader()
        for row in Data:
            writer.writerow(row)