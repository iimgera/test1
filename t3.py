class Beks:
    def __init__(self, name):
        self.name = name
        self.age = 21
        self.gender = 'male'

    def calculate_age(self):
        print(self.age + 15)
        
b = Beks("Beksultan")
b.calculate_age()