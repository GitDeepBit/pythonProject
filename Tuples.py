# Tuples are immutable: Meaning once they are assigned a value, it cannot be updated in any way

tuple1 = (1, 2, "tuple value", 50.768, 1, 1, 2, 1, 2)

print(tuple1)

# TypeError: 'tuple' object does not support item assignment
# tuple1[1] = "44"

# Returns the number of occurrence of the value from tuple which is passed in count function as an argument
print(tuple1.count(1))
print(tuple1.count(2))