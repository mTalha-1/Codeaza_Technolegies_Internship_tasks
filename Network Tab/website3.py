import requests

i = 1
while i <3:
    print('\nPage',i,' Data')
    url = "https://practiceapi.geeksforgeeks.org/api/vr/problems/?pageMode=explore&page="+str(i)+"&sortBy=submissions"
    headers = {
    'authority': 'practiceapi.geeksforgeeks.org',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7',
    'origin': 'https://practice.geeksforgeeks.org',
    'referer': 'https://practice.geeksforgeeks.org/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    i +=1


# url = "https://practiceapi.geeksforgeeks.org/api/vr/problems/?pageMode=explore&page=2&sortBy=submissions"

# headers = {
#   'authority': 'practiceapi.geeksforgeeks.org',
#   'accept': '*/*',
#   'accept-language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7',
#   'origin': 'https://practice.geeksforgeeks.org',
#   'referer': 'https://practice.geeksforgeeks.org/',
#   'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'same-site',
#   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)
