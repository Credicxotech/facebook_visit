import requests

proxies = {
  "http": "http://178.62.232.131:24000",
  "https": "https://178.62.232.131:24000",
}

r = requests.get('https://www.facebook.com', proxies=proxies,)