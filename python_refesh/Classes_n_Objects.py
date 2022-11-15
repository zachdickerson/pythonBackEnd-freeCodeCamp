# python is a object oriented language

# Know that definition

#Example 1

# class MyClass:

#     # x is a object in myclass
#     x = 5

# p1 = MyClass()
# print(p1.x)

# Example 2

class Person:

    def __init__(self, name, age):
        
        self.name = name 
        self.age = age

name = input("Enter you name: ")
age = int(input('Enter your age: '))
p1 = Person(name, age)
print(p1.name)
print(p1.age)
del p1
print(p1)



