# class Cats:
#     def __init__(self, name, age, location, sound) -> None:
#         self.name = name 
#         self.age = age
#         self.location = location
#         self.sound = sound
#     def get_name(self):
#             return f"Меня зовут {self.name}"
#     def get_location(self):
#         return f"Я из{self.location}"
#     def get_age(self):
#         return f"Мне {self.age}"
#     def get_voice(self):
#         return self.sound
# class Cow:
#     def __init__(self, name, age, location, sound) -> None:
#         self.name = name 
#         self.age = age
#         self.location = location
#         self.sound = sound
#     def get_name(self):
#         return f"Меня зовут {self.name}"
#     def get_location(self):
#         return f"Я из{self.location}"
#     def get_age(self):
#         return f"Мне {self.age}"
#     def get_voice(self):
#         return self.sound
# class Monkey:
#     def __init__(self, name, age, location, sound) -> None:
#         self.name = name 
#         self.age = age
#         self.location = location
#         self.sound = sound
#     def get_name(self):
#             return f"Меня зовут {self.name}"
#     def get_location(self):
#         return f"Я из{self.location}"
#     def get_age(self):
#         return f"Мне {self.age}"
#     def get_voice(self):
#         return self.sound
    
# cat =Cats("tiger", 4, "Almaty", "may")
# cow = Cow("milka", 12, "sweden","muuu bla" )
# monkey = Monkey("king", 24, "Africa", "Uuaaaaa")


# animal = [cat, cow, monkey]

# for i in animal:
#     print(i.get_name())

import requests
from bs4 import BeautifulSoup
import json

class Parser:
    def __init__(self, url, domen):
        self.url = url
        self.domen = domen
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        }
    
    def get_html(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        return f"error: {response.status_code}"

class Amdm(Parser):
    def __init__(self, url, domen):
        super().__init__(url, domen)
        self.data = []
    
    def processing(self):
        soup = BeautifulSoup(self.get_html(), "lxml").find("div", {"class": "content-table"}).find("article", {"class": "g-padding-left"}).find("h1").text
        if soup == "Ничего не найдено":
            print(soup)
        else:
            souppesni = BeautifulSoup(self.get_html(), "lxml").find("div", {"class": "content-table"}).find("article", {"class": "g-padding-left"}).find("table", {"class": "items"}).find_all("tr")
            for acords in souppesni:
                try:
                    name = acords.find("td", {"class": "artist_name"}).find("a", {"class": "artist"}).find_next_sibling().text
                    url = acords.find("td", {"class": "artist_name"}).find("a", {"class": "artist"}).find_next_sibling().get("href")
                    self.data.append({
                        "name": name,
                        "url": url,
                    })
                except Exception as e:
                    print(f"An error occurred: {e}")
                    continue
            with open("Amdm.json", "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False)

amdm1 = Amdm("https://amdm.ru/search/?q=edsheran", "https://amdm.ru")
amdm1.processing()
