import requests

url = "https://www.3m.com/snaps2/api/pcp-show-next/https/www.3m.com/3M/en_US/p/c/abrasives/?size=51&start=51"

payload = {}
headers = {
  'authority': 'www.3m.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7',
  'cookie': 'AKA_A2=A; at_check=true; rxVisitor=1689020774967VME4GILPRPRS25D64UOL9TPQ6IQD9BB4; AMCVS_FEE4BDD95841FCAE0A495C3D%40AdobeOrg=1; s_ecid=MCMID%7C77637616167676741861090717339262908715; AMCV_FEE4BDD95841FCAE0A495C3D%40AdobeOrg=1406116232%7CMCIDTS%7C19549%7CMCMID%7C77637616167676741861090717339262908715%7CMCAAMLH-1689625575%7C3%7CMCAAMB-1689625575%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1689027975s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.5.0; mboxEdgeCluster=38; ak_bmsc=D30C939AB155CBB16757F2E2645D04E1~000000000000000000000000000000~YAAQvbnVF4AP5wKJAQAA68h7QRRHB2wFiUfYwAZPSYhPd+5Nfns4tnR/D56laidxOwciMYgN+cVnpmfyJpudZRvVSCNjj8GJ3KgSWvd+ZexbcC56s8vKKv38Olcy3xT/VAPQZRlnmeWUJ7u9QkB8WreM7BZo3V250PvN8RTatkTO0UN1Iovpx4qeqKqp9nbibRtM/dZi0L1VmLFF0CkJRCsr5VJ26ZUPtgzoM+LalnJdhryOBHOwZHVoK/Spv6oJWlGM8IeCY+bNUXKF9cglsioitwXJgg2wSMCkxtUpzlVdLMXsV9bgfXUtytvKk4BlSUOOSCJDePaabVQ0d8hfPnIQYu0QPfH7HgcoGGMoC9acckS89ol0R3VIH3nvyMuusOn0ffpaajTVCfCiigl/yejaPOuWt8Xc0JxhHipG+vMg2t/fkH5QrfOA+D9r0/fEs37u9EdZj+tVF9FA6RsAMrjcsoqFJGMaQJo2SVbCQJPcgsqBOT+5; BVBRANDID=3ecb3534-e104-43dc-9c7a-3422aac15e03; BVBRANDSID=5cc05340-6442-4cbb-811b-16af5678b885; ELOQUA=GUID=846F9B2BC3554421832E2F9A53C802B9; gclid=undefined; s_cc=true; _gcl_au=1.1.643828096.1689020794; ln_or=eyIxNzA5NTUiOiJkIn0%3D; _pin_unauth=dWlkPVltRTFZVGxqTXpFdE5XRTVaUzAwWXprNExUaGtOV010TkdNNE5UZGpOalE0WmpBdw; _tt_enable_cookie=1; _ttp=czebaK0lN7uNhCkMdSa-Dovy7Mt; mdLogger=false; kampyle_userid=4399-be5c-d1da-7d38-54bf-5256-94ff-5388; ee1b5d445b4a4f48723fa58a17090439=d9b03c2380b72a24e6462e8180ead03f; kampylePageLoadedTimestamp=1689020840436; 0f627b32de4b1b5c65ff57c6010a5e0b=e127fc05feeabc02c76602ab60c800da; dtCookie=v_4_srv_17_sn_96H6OI0AISL0VG67GINSPUPTJQH4KV5G_perc_100000_ol_0_mul_1_app-3A51e330a77f3260d5_1_app-3Aea7c4b59f27d43eb_1; dtSa=-; mbox=session^#2b41c0b07f6f47988251e26fcca68981^#1689024061|PC^#2b41c0b07f6f47988251e26fcca68981.38_0^#1752267001; RT="z=1&dm=www.3m.com&si=85494ede-622f-437c-9bd7-ed42cc4f10b5&ss=ljxbynm6&sl=4&tt=esk&obo=2&rl=1"; utag_main=v_id:0189417beca1001cce37a0490b750506f002a0670086e^$_n:1^$_e:41^$_s:0^$_t:1689024004552^$ses_id:1689020787875%3Bexp-session^$_n:8%3Bexp-session^$_revpage:MMM-ext%3Bexp-1689025804749^$vapi_domain:3m.com^$dc_visit:1^$dc_event:41%3Bexp-session^$dc_region:eu-central-1%3Bexp-session; adcloud={%22_les_v%22:%22y%2C3m.com%2C1689024005%22}; _uetsid=118c04401f6011ee9af387fc50e7fa6b; _uetvid=118c62001f6011eeac75491b86f30507; kampyleUserSession=1689022206597; kampyleUserSessionsCount=8; kampyleSessionPageCounter=1; kampyleUserPercentile=83.75247800897911; s_sess=%20tp%3D12083%3B%20s_ppv%3D%252F3M%252Fen_US%252Fp%252Fc%252Fabrasives%252F%252C99%252C89%252C11981%3B; AWSALB=DpdI4pFQ39+sfea9XCea0m2+1u1KooIxISHfgzhSI9fwvh7TIlrpzF5eVh4Lm/aeJmpx083WfilmXXCqaVgApZ0ZxxaF9m7tY1Nf9e9c0Ydg51nZ2MwJr4rsPgaY; AWSALBCORS=DpdI4pFQ39+sfea9XCea0m2+1u1KooIxISHfgzhSI9fwvh7TIlrpzF5eVh4Lm/aeJmpx083WfilmXXCqaVgApZ0ZxxaF9m7tY1Nf9e9c0Ydg51nZ2MwJr4rsPgaY; bm_sv=64A60417E4ED9FB34A33997A0E09FF58~YAAQPSEPF2b6Ji+JAQAAb6SRQRQQL/jxVu4yhyRDhN1Ug95oPrdM8BnW4E+kWgFd+gptxzmlBBUj3uAOLNCNIKPxTWV6xIftRieQAXAxUKbQhDfkitECZ7zxH45n03AgrBIANl15QPZv9FgZsvP5MqjaH4Dd+2x4zUALLeyIe2Yc9u4r/USikZ0XViw/RhKOc/KwSpWHkVESVaAFcQK3AGyP8thRsASoKxTFtLlwbAwp1Ihs/r0JNOrtarwc~1; s_pers=%20gpv_pN%3D%252F3M%252Fen_US%252Fp%252Fc%252Fabrasives%252F%7C1689024016415%3B%20gpv_pURL%3Dwww.3m.com%252F3M%252Fen_US%252Fp%252Fc%252Fabrasives%252F%7C1689024016420%3B; s_sq=3mproduction%3D%2526c.%2526a.%2526activitymap.%2526page%253D%25252F3M%25252Fen_US%25252Fp%25252Fc%25252Fabrasives%25252F%2526link%253DShow%252520more%2526region%253DSNAPS2_root%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253D%25252F3M%25252Fen_US%25252Fp%25252Fc%25252Fabrasives%25252F%2526pidt%253D1%2526oid%253Dfunctionsn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT; rxvt=1689024016433|1689020774970; dtPC=17^$22200220_197h17vNUPRHKOHIPSCVFCFLMTRMWDFAIUVUFRP-0e0; bm_sv=64A60417E4ED9FB34A33997A0E09FF58~YAAQrGV0aOtK4RCJAQAAkm2XQRSbHCrUp2FlRZdVkuS6aGi3tV8zMV/7q4kRu0Y1J+BEMarUyzPBW6D4TH4UIxUrhqD1l6TgLvntSUEL0cR8699AVzd/IAc2Xhlff25QjctQuXlUA5QMMCgcDFDFfWlKO4DtdWf7p8ncC1pJFgzntmP5Svw3QN2v2UFmVxZA5x2OeuqH465cNPX+j+K2I9KSjCI5XHwQBtoIMejMdgi8JPr5Ajle5ZS2hrNX~1; AWSALB=HgjJB5EOmcmJMSrGlFDpeMwOpZc8IfpEeW1Af6L0CGS1UJ8ChE8EQDmrJl6A5octpDH8vgBty+JdUEX9VGWbuOHXrswz878g9wWEwqTGPMRabNvSR5gRzc7dYMvf; AWSALBCORS=HgjJB5EOmcmJMSrGlFDpeMwOpZc8IfpEeW1Af6L0CGS1UJ8ChE8EQDmrJl6A5octpDH8vgBty+JdUEX9VGWbuOHXrswz878g9wWEwqTGPMRabNvSR5gRzc7dYMvf',
  'referer': 'https://www.3m.com/3M/en_US/p/c/abrasives/',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'x-dtpc': '17^$22200220_197h17vNUPRHKOHIPSCVFCFLMTRMWDFAIUVUFRP-0e0'
}

response = requests.request("GET", url, headers=headers, data=payload)

res = response.json()
#print(res.keys())
#print(type(res['items']))
print(res['items'][0]['url'])

