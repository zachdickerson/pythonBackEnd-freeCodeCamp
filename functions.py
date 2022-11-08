


def greetings():
    print('Hello World')
# This is how to run the function in Visual Studio
#greetings()


def greeting_funciton(name, age):
    print(f'Welcome {name} you are {age} years old.')

#greeting_funciton('John', 27)


#Passing various amounts like a list

def greetings2(*names):
    print(f'Welcome {names[1]}')

#greetings2('john','zach', 'jeff')

def my_function():
    return 5+4

#print(my_function())

def add_numbers(num1,num2):
    return num1+num2

num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
print(add_numbers(num1,num2))