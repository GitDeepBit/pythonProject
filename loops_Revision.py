list2 = [2, 3, 5, 8, 13]

print("List values using loop")
for i in list2:
    print(i)

print("List values multiple by 2")
for i in list2:
    print(i*2)

summation = 0
print("Sum of natural numbers using loop and function range")
# Here range will be of number 1-5, considering last index given in range is index - 1
# for(j=1;j<6;j++): Syntax from other languages
for j in range(1, 6):
    summation = summation + j

print(summation)


summation = 0
list3 = [1, 2, 3, 4, 5]
print("Sum of natural numbers using loop and list from 1-5")
# Here range will be of number 1-5, considering last index given in range is index - 1
for j in list3:
    summation = summation + j

print(summation)


# Incrementing the counter from +1 to +2 or +3 etc.
print("Loop will be used to print range of values but with incremental counter of 2")
for j in range(1, 11, 2):
    print(j)

# Using range function without giving first index. In that case, the first index will be considered as 0 instead of 1
print("Loop will be used to print range of values but the first index will be defaulted to 0 as it is not passed")
for j in range(11):
    print(j)
