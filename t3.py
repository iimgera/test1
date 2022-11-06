class Beks:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
       
    def calculate_age(self): 
        print(self.age + 15)

b = Beks("Beksultan", 21, "male")
print("Через 15 лет " + b.name + " исполнится")
b.calculate_age()

