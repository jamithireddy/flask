# print((2+10)*(3+10))
# myList = [1, 2, 3, 4]
# print(myList)
# print(len(myList))

# mypairs = [(1, 'a'), (2, 'f'), (6, 'p')]
# # Tuple unpacking
# for item1, item2 in mypairs:
#     print(item1)
#     print("the key is" + item2)
class Dog():
    # Class Object Atributes
    no_of_legs = 4

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


x = Dog('poodle', 'penky')

print(x.breed)
print(x.name)
print(x.no_of_legs)
