class Animal():
    def __init__(self):
        print('koiii')

    def dog(self):
        print('bark!!!')

    def cat(self):
        print('Meow!!!')

class Bird(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('hkjh')

