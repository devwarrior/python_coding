''' using list with python '''
LIST_A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
LIST_B = [0, "word", "another word", 3.01, 4, 5, 6, 7, 8, 9]

print(LIST_A)
print(LIST_B)


print(LIST_A[2])
print(LIST_B[1])

print(LIST_A[2:5])

# append elements to a list
LIST_A.append(8)
print(LIST_A)

# remove elements from a list
# remove first occurence of 8 in lista
LIST_A.remove(8)
print(LIST_A)

print("LIST_REM")
LIST_REM= LIST_A[:]
print(LIST_REM)
del LIST_REM[2]
print(LIST_REM)
del LIST_REM[0:2]
print(LIST_REM)


print('insert in the middle')
# insert element in the middle of the list
LENGTH = len(LIST_A)
POS = int(LENGTH / 2)
LIST_A.insert(POS, 100)
print(LIST_A)


print('reverse and sort')
# reverse the list
REV = list(reversed(LIST_A))
print(REV)

# sort LISTA
SORTED = list(sorted(LIST_A))
print(SORTED)

