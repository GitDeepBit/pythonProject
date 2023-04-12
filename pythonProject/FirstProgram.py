print("hello")

a, str1 = 3, "World"

print(a)

b, c, d, e = 5, 6.5, "Hello", 80

print(b, c, d)

# Concatenation for different data types

# This returns string value by using format function to convert it into string.
# Braces are used to signify the position of string variables

print("{} {}".format("Hello", e))
print("{} {} {} {}".format("Value is", b, "& the other value is", c))

# Concatenation of same data types

print("Say"+" "+d+" "+str1)

# To know your data type

print(type(b))

print(type(c))

print(type(d))

#List

newlist = []

print(newlist)

newlist[0] = "Hello"

listvalues = [1, 8, "Punjabi", 80, 90]


print(listvalues[0])

print(listvalues[3])
print(listvalues[-1])  # Last value, -1 represent end of list a.k.a last index
print(listvalues[0:4])  # Range of values

listvalues.insert(3, "oye hoye")  # Inserting a new value in any index
print("Insert:", listvalues)

listvalues.append("Purey 100")  # Inserting value at the end of the list
print("Append:", listvalues)

# Extend can add one or more multiple values at the end of the list but append can only add one value,
# Either a list as a single value or any single value

listvalues.extend(["Hello", 40, "Punjabi"])
print("Extend:", listvalues)

listvalues.append([10, 40, "Yellow"])
print("List Appended inside a list:", listvalues)

listvalues[2] = "PUNJABI"  # Updating value at a certain index
print("Updating value on an index: ", listvalues)

del listvalues[0]  # Deleting values at a certain index

print("Deleting value at 0 Index", listvalues)

# Tuple is immutable: Mein jaisa hu waisach rahunga

tuplevalues = (1, 3, "ahu", 7.9)

# tuplevalues[2] = "AHU AHU" # Values cannot be update in tuples

print(tuplevalues)

# Dictionary: Key and values

dictvalues = {1:"First", "StringKey Num Value": 2, "String Key": "String Value"}

print(dictvalues)
print(dictvalues[1])
print(dictvalues["StringKey Num Value"])
print(dictvalues["String Key"])
# print(dictvalues["String Value"]) - Values cannot be passed in dictionary as indicators, only key can be passed

# Empty Dictionary

newdict = {}

newdict[1] = "First"
newdict[2] = "Second"
newdict["Name"] = "Deep"
newdict["Last Position"] = 4

print(newdict)
print(newdict["Name"])



