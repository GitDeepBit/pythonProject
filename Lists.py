list1 = [1, 4, "Deep", 70, 40.5]

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

print("Below output will be list of values from starting index to last mentioned index -1")
print(list1[1:4])

print("Below output will be the value from last index")
print(list1[-1])

print("Below output will be insertion of new values at a certain index and increasing the size of list")
list1.insert(3, "Singh")
print(list1)

print("Below output will append new values at the end of the list and increasing the size of list")
list1.append("End Of the List")
print(list1)

print("Modifying value at a certain index value")
list1[2] = "DEEP"
print(list1)

print("Below output will delete values at a certain index")
del list1[4]
print(list1)
