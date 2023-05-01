
# We take inputs using function input. It takes statement and when user enters a value on the console, it will return
# the value as str
greeting = input("Enter a message: ")

if greeting == "Morning":
    print("Condition matched")
else:
    print("Condition is not matched")

print("This is out of If Else block")
print(type(greeting))

numberVal = input("Enter a value: ")

if int(numberVal) == 2:
    print("Condition matched")
else:
    print("Condition is not matched")

print("This is out of If Else block")
print(type(numberVal))

