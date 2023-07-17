import requests
from bs4 import BeautifulSoup
class Parser:
    def __init__(self, url) -> None:
        self.url  = url
        self.headers = {

            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
        }
        self.proccessing ()
    def get_html(self):
        response = requests.get(url=self.url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            return FileExistsError("Error", response.status_code)
    # def proccessing (self):
    #     soup = BeautifulSoup(self.get_html(), "lxml")

class Site1(Parser):
    def __init__(self, url) -> None:
        super().__init__(url)
    def proccessing (self):
        soup = BeautifulSoup(self.get_html(), "lxml")
        
class Site2(Parser):
    def __init__(self, url) -> None:
        super().__init__(url)
    def proccessing (self):
        soup = BeautifulSoup(self.get_html(), "lxml")

site = Site1("https://www.google.com")
site2 = Site2("https://www.google.com3")

polimorfismo = [site, site2]
for i in polimorfismo:
    print(i.processing())