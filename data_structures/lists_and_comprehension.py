''' using list with python '''
LISTA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(LISTA)
# append elements to a list
LISTA.append(8)
LISTA.append(8)
print(LISTA)

# remove elements from a list
# remove first occurence of 8 in lista
LISTA.remove(8)
print(LISTA)

# reverse the list
REV = list(reversed(LISTA))
print(REV)

# insert element in the middle of the list
LENGTH = len(LISTA)
POS = int(LENGTH / 2)
LISTA.insert(POS, 100)
print(LISTA)


# sort LISTA
SORTED = list(sorted(LISTA))
print(SORTED)


# list comprehension
# we can populate a list using append as follows:
NEWLIST = []
for counter in range(10):
    NEWLIST.append(counter)
print(NEWLIST)
# these three lines fills NEWLIST with these values:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# The above code has a side effects, it creates or overwrites
# the variable named counter

# instead we can use list comprehension, the same list will be generated by
LIST_COMP_1 = [x for x in range(10)]

# one line vs 3, and without side effects. This is the pythonic
# way of list generation
print(LIST_COMP_1)

# naturally you can do more complex lists:
LIST_COMP_2 = [x**2 for x in range(10)]
print(LIST_COMP_2)

#imagine you want to create a new list containing all elements of list_comp_2 that are even
# with normal code:
LIST_COMP_3 = []
for elem in LIST_COMP_2:
    if elem % 2 == 0:
        LIST_COMP_3.append(elem)
print(LIST_COMP_3)

#the same list using list comprehension
LIST_COMP_4 = [x for x in LIST_COMP_2 if x%2 == 0]
print(LIST_COMP_4)


# last example all elements contained in both LIST_COMP_2 and LIST_COMP_1
# that are even
LIST_COMP_5 = [x for x in LIST_COMP_2 if x in LIST_COMP_1 and x%2 == 0]
print(LIST_COMP_5)

# the same list without using list comprehension
LIST_6 = []
for elem in LIST_COMP_2:
    if elem in LIST_COMP_1:
        if elem%2 == 0:
            LIST_6.append(elem)
print(LIST_6)
