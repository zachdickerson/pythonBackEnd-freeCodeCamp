
# try:
#     x = int(input('Input an Integer: '))
#     print(x)
# except:
#     print('value not a integer.. Please try again')


# try:
#     x = int(input('Input an Integer: '))
#     print(x)
# except ValueError:
#     print('Value not a integer')

try:
    x = int(input('Input an Integer: '))
    print(x)
except:
    print('Something went wrong')
finally:
    print('try except finished')

try:
    x = int(input('Input an Integer: '))
    print(x)
except:
    print('Something went wrong')
else:
    print('ntohing went wrong')