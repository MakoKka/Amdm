from time import sleep

class Human:
    def __init__(self, name, school, klass, uroki, bag) -> None:
        self.name = name 
        self.school = school
        self.klass = klass
        self.uroki = uroki
        self.bag = bag
    def get_name(self):
        return f"Меня зовут {self.name}"
    def get_school(self):
        return f"Я учусь в {self.school}"
    def get_klass(self):
        return f"в {self.klass}"
    def get_uroki(self):
        uroki = ['matem', 'fizika']
        return uroki
human = Human("Maks", "62", "9v", )

print(human.get_name)
    