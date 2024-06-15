import requests
from bs4 import BeautifulSoup

res= requests.get("https://www.geeksforgeeks.org/")

soup=BeautifulSoup(res.content,"html.parser")

print(soup.prettify())