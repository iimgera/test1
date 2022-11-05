class Monkey():
    max_age = 12
    loves_bananas = True

    def climb(self):
	    print('I am climbing the tree')

orang = Monkey()
mac = Monkey()

print('My max age -', orang.max_age,'. I love bananas and its -',orang.loves_bananas)
orang.climb()

print('My max age -', mac.max_age,'. I love bananas and its -',mac.loves_bananas)
mac.climb()

