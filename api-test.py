import requests
from bs4 import BeautifulSoup

url = "https://httpbin.org/"
ans = requests.get(url)

#print(ans.content)
x = BeautifulSoup(ans.text,'html')
print(x.prettify)

