ae = "{} {}".format("Hello", 10)

print(type(ae))

listvalues = [1, 8, "Punjabi", 80, 90]

newlist = []

print(newlist)

#  newlist[0] = "Hello"
newlist.append("Hello1")
newlist.insert(2, "Hello")
# Flaw bhains ki aankh but itni bhi nahi
# If the list is empty then by default it will insert the value at 0th index even though the assignment was done at a
# Different index value

print(newlist[0])
print(newlist)
print("Coverted List into Tuple:", tuple(newlist))

raisin = {1: "Yolo", 2: 45, "e": "Show off menu karna penda", 69: "Namuna"}

print(raisin.keys())
print(raisin.values())

# This returns key, value of dictionary as a tuple
print(raisin.items())

#  The only way to append and insert values at the end
raisin[4] = 5
print(raisin)

# This is updating value on a certain key just like list. But here we have key, there we have index
raisin[1] = "Hello"
print(raisin)

# This is an update which works like extend if we are inserting new values. This is updating dict with new values
raisin.update({"deep": "values", 50: "Namuna"})
print(raisin)

# This also update values on multiple key in one go
raisin.update({1: 4, 2: "Yolo"})
print(raisin)

raisin.update({69: "Brampton"})
print(raisin)

raisin.update({45: "e", "Yolo": 1})
print(raisin)



for chabbi in raisin.keys():
    print(chabbi)

print("************************************")

for chabbi in raisin.values():
    print(chabbi)

print("************************************")

for chabbi, taala in raisin.items():
    print((chabbi, taala))