import requests
from fake_useragent import UserAgent

splash_url = "http://192.168.99.100:8050/render.html?url={}&wait=1"
url = "https://www.guazi.com/bj/buy/"
response = requests.get(splash_url.format(url), headers={"User-Agent": UserAgent().random})
response.encoding = 'utf-8'
print(response.text)
