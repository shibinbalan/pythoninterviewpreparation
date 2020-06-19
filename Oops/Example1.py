class Dog():
    species = 'mammal'
    def __init__(self,breed,colour):
        self.breed = breed
        self.colour = colour

    def bark(self,number=0):
        print(f'myname is {self.breed} and {number}')


my_dog = Dog(breed='Lab',colour='Pacha')
print(my_dog.colour)
print(my_dog.species)
print(my_dog.bark())