strVar1 = "String1.strVar1"
strVar2 = "String2.strVar2"
strVar = "String1"
strVar3 = " Hello "

strMain = "Please email us at mentor@rahulshettyacademy.com with below template to receive response"

print(strVar1[3])

print(strVar2[0:7])

print(strVar1+" "+strVar2)

print(strVar in strVar1)

print(strVar in strVar2)

# Split function makes the result of string to a list based on splitter
var = strVar1.split(".")

# Output will be in a list as: ['String1', 'strVar1']
print(var)

# This will print the [0]th Index of list that was created via split of String, refer line 20
print(var[0])

# This strips spaces from left and right of the string
var1 = strVar3.strip()

# Output will be Hello without the first and the last space in the string
print(var1)

# There are two more methods: lstrip() and rstrip()
# lstrip() removes spaces from the left side/beginning of the String
# rstrip() removes spaces from the right side/end of the string

# Index [1] and [0] represents the index of the list we have extracted
var2 = strMain.split("at")[1].strip().split(" ")[0]

print(var2)