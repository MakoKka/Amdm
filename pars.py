
import json
from bs4 import BeautifulSoup
import requests

URL = "https://amdm.ru/search/?q=" +input("Search ")
DOMEN ="https://amdm.ru/"
HEADERS = {
    "User-Agent":
	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    
}

response = requests.get(url=URL, headers=HEADERS)
with open("amdm.html", "w")as responsave:
    responsave.write(str(response.text))

soup =BeautifulSoup()
