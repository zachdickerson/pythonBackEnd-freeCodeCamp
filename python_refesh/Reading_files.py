# open('my_file.txt', 'r') # reading the file

# open('my_file.txt', 'w') # writing to the file

# open('my_file.txt', 'a') # appending to the file

# open('my_file.txt', 'r+') # read and write

# if text file or file is in another directory grab whole file path and 
# swith the \ to /

# count_file = open('my_file.txt', 'r')
# print(count_file.readlines())
# count_file.close()

# count_file = open('my_file.txt', 'r')
# for lines in count_file.readlines():
#     print(lines)
# count_file.close()


# writing to the existing file in python , which is appending text to the file
count_file = open('my_file.txt', 'w')
count_file.write('This is a new file')

#creating a new file
count_file = open('country.txt', 'w')
count_file.write('This is a new file')
#append new text to new country file
count_file.write('\nThis is a new line')

