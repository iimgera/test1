class Cats:
    name = 'Minni'
    noise = 'Meow!'
    action = 'yawned'

    def behavior(self):
        print(self.name, self.action, 'and said:', self.noise)

cat = Cats()
cat.behavior()


