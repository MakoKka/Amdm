class Person:
    def __init__(self, name , age, last_name, gender, bithrday, wight, height) -> None:
        self.name = name
        self.age = age
        self.last_name = last_name
        self.gender = gender
        self.bithrday = bithrday
        self.weight = wight
        self.height = height      
    def __main_info(self):
        return
class People_1(Person):
    def __init__(self, name, age, last_name, gender, bithrday, wight, height, job, country, national, 
        language, race, deegre: bool, status:bool) -> None:
        
        
        super().__init__(name, age, last_name, gender, bithrday, wight, height)
        self.job = job
        self.county = country
        self.nationality = national
        self.language = language
        self.race = race
        self.deegre = deegre
        self.status = status


        def main(self):
            return super().__main_info()
        def action(self):
            list_action = [
                f'я {super().name} проснулся уммылся'
                f"я {super().name}вышел погулять"
                f"я {super().name} и у меня сегодня день рождения "
                f"я {super().name} и я лежу дома"
                f"я {super().name}"
            ]