"""
    Homework 5, Exercise 3
    Nick Waggoner
    11-7-2021
    Description: This program uses a generator to recreate the range()
    function for the purpose of reserving memory.
"""

#from sys import getsizeof


def genrange(stop, start=0, step=1):
    # stop is not included in the range
    x = start
    if step == 0:
        print("Step may not be 0")
    elif stop < start and step < 0:
        # Deals with negative case
        while x > stop:
            yield x
            x = x + step
    elif start < stop and step > 0:
        # Deals with working positive case
        while x < stop:
            yield x
            x = x + step
    else:
        print("Invalid input arguments")

for i in genrange(6, 3):
    print(i)
print()
for i in genrange(6):
    print(i)
print()
for i in genrange(-5, 0, -1):
    print(i)
print()

"""
#Checking out the sizes of the objects
list_comp = [x *5 for x in range(1000)]
gen_exp = (x * 5 for x in genrange(1000))

print(getsizeof(list_comp))
print(getsizeof(gen_exp))
"""