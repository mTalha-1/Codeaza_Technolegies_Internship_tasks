import requests
import json
i = 10
while i< 30:
    print('\n Next Page Data')
    url = "https://www.hackerrank.com/rest/contests/master/tracks/python/challenges?offset="+str(i)+"&limit=10&track_login=true"

    headers = {
    'authority': 'www.hackerrank.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7',
    'content-type': 'application/json',
    'cookie': 'hackerrank_mixpanel_token=0805f848-afcb-4052-8ae8-e440a5237581; _ga=GA1.2.324096814.1671535896; _pk_id.5.fe0a=cfe56a98c246b3d4.1671535898.; show_cookie_banner=false; mp_bcb75af88bccc92724ac5fd79271e1ff_mixpanel=%7B%22distinct_id%22%3A%20%220805f848-afcb-4052-8ae8-e440a5237581%22%2C%22%24device_id%22%3A%20%221856df4b92e244-04a5e1dc77259-26021151-100200-1856df4b92f2e5%22%2C%22%24user_id%22%3A%20%220805f848-afcb-4052-8ae8-e440a5237581%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; _wchtbl_uid=b84a422b-1973-41cb-b140-60cc4fd5b4e8; _gd_visitor=5957fead-545c-4cd8-8f19-a72decac6434; _uetvid=3d88c34089e911ed831f4150bafd30e5; _gd_svisitor=8232d417a65e00004708926336020000e9661c00; user_theme=dark; __utmz=74197771.1673714905.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _biz_uid=991ba9f7425b403efc88b1b19522b7a5; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; _hjSessionUser_2036154=eyJpZCI6ImFmZTc3ZGRiLTI2YTMtNTk2MC04NzdmLTM1NzE2ZDI3NDNiNyIsImNyZWF0ZWQiOjE2NzM3MTM2MTYwNDksImV4aXN0aW5nIjp0cnVlfQ==; _pk_ref.5.fe0a=%5B%22%22%2C%22%22%2C1685350722%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; enableIntellisenseUserPref=true; hacker_editor_theme=light; __utma=74197771.324096814.1671535896.1686150867.1686150867.3; _biz_nA=5; _biz_pendingA=%5B%5D; react_var=false__cnt6; react_var2=false__cnt6; user_type=hacker; _gid=GA1.2.1211213541.1689583279; remember_hacker_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaGJDRnNHYVFTR0xUc0JJaUlrTW1Fa01UQWtWbTlMZGpWdlltUkhUVXgxWm1OM1pVRXhRVE5WZFVraUZ6RTJPRGsxT0RNeU9UVXVPRFl4TnpNNU9RWTZCa1ZHIiwiZXhwIjoiMjAyMy0wNy0zMVQwODo0MTozNS44NjFaIiwicHVyIjpudWxsfX0%3D--446b711fc34445cb595b91852a6b4a860b5572c0; hrc_l_i=T; metrics_user_identifier=13b2d86-ced931858a6bf234addb3816ad1f08f97ce35c25; _hrank_session=451250f8ed0e9c026ebe38c285a90474; _hp2_ses_props.547804831=%7B%22ts%22%3A1689643946693%2C%22d%22%3A%22www.hackerrank.com%22%2C%22h%22%3A%22%2Fdashboard%22%7D; _hjIncludedInSessionSample_2036154=0; _hjSession_2036154=eyJpZCI6IjZiNzY1NTVmLWEyMmMtNGNlZS1iNWY5LTc0NjBlNjE5OTk1YiIsImNyZWF0ZWQiOjE2ODk2NDM5NDg4NDMsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gat_UA-45092266-28=1; _gat_UA-45092266-26=1; _hp2_id.547804831=%7B%22userId%22%3A%227347165882754735%22%2C%22pageviewId%22%3A%224736114835759245%22%2C%22sessionId%22%3A%22368041581015107%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
    'if-none-match': 'W/"26192986f374f0625b32510746d0ebc1"',
    'referer': 'https://www.hackerrank.com/domains/python',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-csrf-token': 'n5yg0aVDq3VbWcyWfi0rZ8PAurAw4/ppzOOFsYqI9Dx+IXS/3LTy9bUsF8rGpMU0B1OND47eXSegOl+G7eLdoQ=='
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    i +=10

# url = "https://www.hackerrank.com/rest/contests/master/tracks/python/challenges?offset=20&limit=10&track_login=true"

# headers = {
#   'authority': 'www.hackerrank.com',
#   'accept': 'application/json',
#   'accept-language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7',
#   'content-type': 'application/json',
#   'cookie': 'hackerrank_mixpanel_token=0805f848-afcb-4052-8ae8-e440a5237581; _ga=GA1.2.324096814.1671535896; _pk_id.5.fe0a=cfe56a98c246b3d4.1671535898.; show_cookie_banner=false; mp_bcb75af88bccc92724ac5fd79271e1ff_mixpanel=%7B%22distinct_id%22%3A%20%220805f848-afcb-4052-8ae8-e440a5237581%22%2C%22%24device_id%22%3A%20%221856df4b92e244-04a5e1dc77259-26021151-100200-1856df4b92f2e5%22%2C%22%24user_id%22%3A%20%220805f848-afcb-4052-8ae8-e440a5237581%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; _wchtbl_uid=b84a422b-1973-41cb-b140-60cc4fd5b4e8; _gd_visitor=5957fead-545c-4cd8-8f19-a72decac6434; _uetvid=3d88c34089e911ed831f4150bafd30e5; _gd_svisitor=8232d417a65e00004708926336020000e9661c00; user_theme=dark; __utmz=74197771.1673714905.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _biz_uid=991ba9f7425b403efc88b1b19522b7a5; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; _hjSessionUser_2036154=eyJpZCI6ImFmZTc3ZGRiLTI2YTMtNTk2MC04NzdmLTM1NzE2ZDI3NDNiNyIsImNyZWF0ZWQiOjE2NzM3MTM2MTYwNDksImV4aXN0aW5nIjp0cnVlfQ==; _pk_ref.5.fe0a=%5B%22%22%2C%22%22%2C1685350722%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; enableIntellisenseUserPref=true; hacker_editor_theme=light; __utma=74197771.324096814.1671535896.1686150867.1686150867.3; _biz_nA=5; _biz_pendingA=%5B%5D; react_var=false__cnt6; react_var2=false__cnt6; user_type=hacker; _gid=GA1.2.1211213541.1689583279; remember_hacker_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaGJDRnNHYVFTR0xUc0JJaUlrTW1Fa01UQWtWbTlMZGpWdlltUkhUVXgxWm1OM1pVRXhRVE5WZFVraUZ6RTJPRGsxT0RNeU9UVXVPRFl4TnpNNU9RWTZCa1ZHIiwiZXhwIjoiMjAyMy0wNy0zMVQwODo0MTozNS44NjFaIiwicHVyIjpudWxsfX0%3D--446b711fc34445cb595b91852a6b4a860b5572c0; hrc_l_i=T; metrics_user_identifier=13b2d86-ced931858a6bf234addb3816ad1f08f97ce35c25; _hrank_session=451250f8ed0e9c026ebe38c285a90474; _hp2_ses_props.547804831=%7B%22ts%22%3A1689643946693%2C%22d%22%3A%22www.hackerrank.com%22%2C%22h%22%3A%22%2Fdashboard%22%7D; _hjIncludedInSessionSample_2036154=0; _hjSession_2036154=eyJpZCI6IjZiNzY1NTVmLWEyMmMtNGNlZS1iNWY5LTc0NjBlNjE5OTk1YiIsImNyZWF0ZWQiOjE2ODk2NDM5NDg4NDMsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gat_UA-45092266-28=1; _gat_UA-45092266-26=1; _hp2_id.547804831=%7B%22userId%22%3A%227347165882754735%22%2C%22pageviewId%22%3A%224736114835759245%22%2C%22sessionId%22%3A%22368041581015107%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
#   'referer': 'https://www.hackerrank.com/domains/python',
#   'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'same-origin',
#   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#   'x-csrf-token': 'n5yg0aVDq3VbWcyWfi0rZ8PAurAw4/ppzOOFsYqI9Dx+IXS/3LTy9bUsF8rGpMU0B1OND47eXSegOl+G7eLdoQ=='
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)
