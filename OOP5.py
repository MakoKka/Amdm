class Animals:
    def __init__(self, tail, legs) -> None:
        self.tail = tail
        self.legs = legs
        last_name = ["pika", "ivan", "koke"]
    def get_info(self):
        print("GGGG")
class Cat(Animals):
    def __init__(self,tail, legs, name, age, poroda) -> None:
        super().__init__(tail, legs)
        self.name = name
        self.age = age
        self.poroda = poroda
    def get_name(self):
        super().get_info()
        return f"name: {self.name}"

# class Dog(Animals):
#     def __init__(self,tail, legs, name, age, poroda) -> None:
#         super().__init__(tail, legs)
#         self.name = name
#         self.age = age
#         self.poroda = poroda
#     def get_name(self):
#         super().get_info()
#         return f"name: {self.name}" 

my_cat = Cat(True, 4 , "hina", 2 , "bot")
print(my_cat.get_name())
print(my_cat.get_info())