import requests

url = "https://colorhunt.co/php/feed.php"
i = 1
while i <3:
    print('\nPage',i,' Data')

    payload = "step="+str(i)+"&sort=new&tags=&timeframe=30"
    headers = {
    'authority': 'colorhunt.co',
    'accept': 'text/html, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': '_gid=GA1.2.1816788319.1689613805; _gat=1; _ga=GA1.2.1636725010.1684686600; _ga_P464R9CGC0=GS1.1.1689620990.19.1.1689621097.49.0.0',
    'origin': 'https://colorhunt.co',
    'referer': 'https://colorhunt.co/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    i +=1


# url = "https://colorhunt.co/php/feed.php"

# payload = "step=1&sort=new&tags=&timeframe=30"
# headers = {
#   'authority': 'colorhunt.co',
#   'accept': 'text/html, */*; q=0.01',
#   'accept-language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7',
#   'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#   'cookie': '_gid=GA1.2.1816788319.1689613805; _ga=GA1.2.1636725010.1684686600; _ga_P464R9CGC0=GS1.1.1689620990.19.1.1689621097.49.0.0',
#   'origin': 'https://colorhunt.co',
#   'referer': 'https://colorhunt.co/',
#   'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'same-origin',
#   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#   'x-requested-with': 'XMLHttpRequest'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
