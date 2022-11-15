countries = ['USA', 'Spain', 'Ghana', 'Rome']
countries2 = list(('USA', 34, False))
print(countries)
print(countries2)
print(countries[0][1])

##### List Methods #####

list1 = [1,2,3,4,5]
list2 = ['banana', 'apples', 'mango', 'oranges']

list1.extend(list2)
print(list1)

list2.append('cherry')
print(list2)

list2.insert(1, 'pear')
print(list2)

list3 = [4,3,5,2,1]
list3.sort()
print(list3)


##### Tuples #####
#Are immutable - meaning cant be manipulated after creation unlike list
three_numbers = (1,2,3)
three_numbers[1] = 23
print(three_numbers) ## this prints error