# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return "description" # f"моя собока зовут{self.name} ему{self.age} года"
    
# my_dog1 = Dog("alf",3)
# my_dog2 = Dog("aktaban",4)

# print(my_dog1.name, my_dog1.age)
# print(my_dog2.name, my_dog2.age)



# class Computer:
#     def __init__(self, name, color, driver, procesor, ram, madein, graph, os,) -> None:
#         self.name =name
        
#         self.color=color
#         self.driver=driver
#         self.procesor=procesor
#         self.ram=ram
#         self.madein =madein
#         self.graph =graph
#         self.os = os
#     def __str__(self) -> str:
#         return f"имя моего компьютера {self.name}, сделано в {self.madein}. Характеристики: driver {self.driver} цвет {self.color},\
#             процессор{self.procesor} оперитивная память {self.ram} график{self.graph} название ОС {self.os}"

# my_comp =Computer("Acer", "black", "NVIDIA GEFORCE GTX", "Intel® Core™ i5-8300H CPU @ 2.30GHz × 8", "1,1 trb", "usa", "NV137 / Mesa Intel® UHD Graphics 630 (CFL GT2)", "Ubuntu 22")

# print(my_comp)


# class Obratno:
#     def __init__(self, slovo) -> None:
#         self.slovo = slovo

#     def reslovo(self):
#         self.slovo = self.slovo[::-1]
#         return self.slovo

# napiwi=Obratno(input("napiwi "))

# print(napiwi.slovo)
# print(napiwi.reslovo())
# print(napiwi.slovo)

# class Audio:
#     def init(self, 
#             name: str,
#             volume: int,
#             next: bool,
#             back: bool,
#             pause: bool
#         ):
#         self.name = name
#         self.volume = volume
#         self.next = next
#         self.back = back
#         self.pause = pause
#         self.music = [
#             "Miyagi - Minor",
#             "Raim - Самая Вышка",
#             "Скриптонит - 360",
#             "Abonent - Povorot",
#         ]
#         self.music_index = 0
    
#     def _volume_up(self):
#         self.volume += 1
    
#     def _volume_down(self):
#         self.volume -= 1

#     def __nexted(self):
#         self.music_index += 1
#         if self.music_index <= len(self.music) - 1: 
#             self.name = self.music[self.music_index]
#         else:
#             self.music_index -=1
    
#     def __backet(self):
#         if self.music_index == 0:
#             self.music_index = len(self.music) - 1
#             self.name = self.music[self.music_index]
#         else:
#             self.music_index -= 1
    
#     def add_music(self, name_music):
#         self.music.append(name_music)
    
#     def _delete_music(self, name_music):
#         self.music.remove(name_music)
    
#     def run(self):
#         while self.pause:
#             table = input(f"""
#     name: {self.name}
#     volume: {self.volume}
#         1: pause
#         2: next
#         3: back
#         4: volume +
#         5: volume -
#         6: add music
#         7: delete music
#     >>> """)
#             if table == "1":
#                 self.pause = False
#             elif table == "2":
#                 self.__nexted()
#             elif table == "3":
#                 self.__backet()
#             elif table == "4":
#                 self._volume_up()
#             elif table == "5":
#                 self._volume_down()
#             elif table == "6":
#                 name_music = input("Напишите название песни\n>>> ")
#                 self.add_music(name_music)
#             elif table == "7":
#                 name_music = input("Напишите название песни для удаления\n>>> ")
#                 self._delete_music(name_music)
#             else:
#                 print("Такой команды нет")


# a = Audio("None", 10, True, False, True)

# print(a.run())