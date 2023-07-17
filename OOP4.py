class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        raise NotImplementedError("Metod get_name() dolchen bit v pod classe")

class Cat(Animal):
    def __init__(self, name) -> None:
        self.name = name
    
    def get_name(self):
        return f"my name is {self.name}"
class Dog(Animal):
    def __init__(self, name) -> None:
        self.name = name
    
    def get_name(self):
        return f"my name is {self.name}"
# нельзя создать экзепляр абстрактного класса Animal
# animal = Animal("animal")

cat1 = Cat("cat")
dog1 = Dog("dog")
a  =[cat1, dog1]

for i in a:
    print(i.get_name())
