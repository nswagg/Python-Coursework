'''
    Homework 2: Exercise 3
    Name: Nick Waggoner
    Date: 9-22-2021
    Description: This program explores various methods for
        manipulating lists and strings. The function
        strList takes in a list as an argument and parses
        through it before printing it back to the user.

    Tags: list, list manipulation
'''

def strList(list):
    str = ''
    for x in range(len(list)-1):
        str = str + (list[x] + ', ')
        continue

    str = str + 'and ' + list[len(list)-1]
    return str

#1
list = ['Wallet', 'Phone', 'Keys']
print(list)
#2
list.sort()
print(list)
#3
print(list[0])
#4
print(list[1:])
#5
print(list[-1])
#6
print(list.index('Keys'))
#7
list.append('Tablet')
print(list)
#8
list.insert(2, 'Mask')
print(list)
#9
list.remove('Phone')
print(list)
#10
list.reverse()
print(list)
#12
print(strList(list))
