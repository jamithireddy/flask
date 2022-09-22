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

# print(x.breed)
# print(x.name)
# print(x.no_of_legs)


# def hello(name='Jose'):
#     print("The hello() function has been run")

#     def greet():
#         return ("    This is inside the greet()")

#     def welcome():
#         return ("    This is inside welcome()")
#     if name == 'Jose':
#         return greet
#     else:
#         return welcome


# x = hello()
# print(x())


def new_decorator(func):
    def wrap_func():
        print("some code before executing func")
        func()
        print("Addiotional code after func()")
    return wrap_func


def plain_func():
    print("Simple code")


plain_func()


plain_func = new_decorator(plain_func)
plain_func()

# The decorator simply added some more code before and and after a simple function by just calling the same function .
# since plain_func = new_decorator(plain_func) looks cumbersome, we shall use '@' decorator as below

# @new_decorator
# def plain_func():
#     print("Simple code")
# plain_fun()       <- with the @ decorator above this is equivalent to plain_func = new_decorator(plain_func)
