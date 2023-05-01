# var = input("Input any value: ")
var = 2
var1 = 10
var2 = 11
a = 0

# Below Loops are endless while loops and while loops cannot be stopped until and unless condition is false
# For that we need decremental/incremental counter inside the loop to make the condition false
while var <= 4:
    print("Value of var", var)
    var = var + 1

print("Outside first while loop")

while var1 >= 4:
    print("Value of var1", var1)
    var1 = var1 - 1

print("Outside second while loop")

# Breaking the while loops or continuing the while loops
# Break function will break the loop if the  condition matches and comes outside the while loop
# Continue function will skip the loop if the condition matches, skipping the loops means that skipping lines from
# if var1 == 6 to var1 += 1

while var2 >= 3:
    if var2 == 8:
        var2 -= 1
        # If this counter is not here, then this loop will become infinite loop
        # And it will be stuck at a certain stage which in this case will be var 2 == 8
        # Output screen will be stuck at var 2 == 9
        continue
    if var2 == 4:
        break
    print("Value of var2", var2)
    var2 -= 1
