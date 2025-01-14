# create a beast class that will store a list of animals
class Pet: # Beast class
    def __init__(self,kind, name): # constructor method
        self.kind = kind
        self.name = name

    def eat(self, food):
        self.food = food

class Dog(Pet):
    def __init__(self, breed, name):
        super().__init__('dog', name)
        self.breed = breed
        self.name = name

    def abort(self):
        print(f"{self.name} abort!")

'''
if __name__ == "__main__": # run the code below if this file is run directly
    my_pet = Pet("My Beast")
    my_pet.add_animal("Dog", "Rex", "Labrador")
    my_pet.add_animal("Cat", "Whiskers", "Siamese")
    my_pet.show_animals()

    my_pet.search_animals("Rex")
    my_pet.search_animals("Whiskers")
    my_pet.search_animals("Fluffy")
'''