#  To get input from user
str1 = input("Say something ")
# Here we have converted the input argument to integer as the value we are passing is integer
a = int(input("Please enter any integer value less than 10 "))

if str1 == "Hello":
    print("Hell Yeah")
    print("Lets go")
else:
    print("Hell Nah")

print("Sab kuch khatam ho gaya")

if a < 10:
    print("Punjabi")
else:
    print("Cry Cry")

print("Sab firse khatam ho gaya")

#  Traversing List
loopobj = [1, 5, 9, 10, 90]
print("List values are:")
for i in loopobj:
    print(i)

print("************************************")
# Range of values -> range(a,b) -> a to b-1 -- for(i=0;i<9,i++)
summ = 0
for j in range(1, 9):
    summ += j

#  Outside the loop
print("Sum of j is ", summ)

print("************************************")

#  how to define value for increment counter -- By default it is +1
for l in range(1, 10, 3):
    print(l)

print("************************************")

#  without starting index, meaning starting with 0 index
for m in range(10):
    print(m)

#  Three ways to iterate loop -- with defined list, with defined range, with defined range and incremental counter
#  And last with no starting index, by default it will be 0

print("************************************")

newvar = int(input("Enter the freaking variable: "))

while newvar >= 2:
    if newvar == 8:
        newvar = newvar - 1
        continue
        # This will make the code go to print(newvar)
        print("Continue block")
    if newvar == 3:
        break
        # This will make the code go out of loop. Code will go to print("While loop ends")
        # End of IF
    print(newvar)
    newvar = newvar - 1

print("While loop ends")

#  "Continue" only skips the block inside the loop and tells the program to continue with other conditions
#  But "Break" indicates that discontinue the coming interation and close the look

# We can traverse a string using loops
strj = "Hello"

for i in strj:
    print(i)

