import requests
from fake-useragent import UserAgent

mycookies_fromcopy = '''bid=xf8i44bKKZU; ll="118160"; dbcl2="249196084:Q9lFQ1CmS7o"; push_noty_num=0; push_doumail_num=0; 
__utmv=30149280.24919; gr_user_id=e918ba5a-49ba-4011-bbdc-b3af0cbe6758; _ga=GA1.1.1272172402.1648469018; 
_ga_RXNMP372GL=GS1.1.1648477884.2.0.1648477884.60; ck=6pMm; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1650504978%2C%22https%3A%2F%2Fwww2.bing.com%2F%22%5D; 
_pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.780128603.1647928768.1650166939.1650504978.9; __utmc=30149280; 
__utmz=30149280.1650504978.9.4.utmcsr=www2.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; _pk_id.100001.8cb4=35d317698a04335b.1648387530.6.1650504986.1650166939.; 
__utmb=30149280.9.9.1650504986438'''
ua = UserAgent()
headers = {'User-Agent':ua.random,'Cookies':mycookies_fromcopy}

url = 'https://www.douban.com/people/249196084/'
data = requests.get(url,headers = headers)

print(data.status_code)
print(data.request.headers)
print(data.text)