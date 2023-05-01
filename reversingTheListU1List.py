# Taking inputs from user and inserting the values in an empty List
# Printing the output of the list - To check
# Opening the file in write mode and writing the lines using w+ feature
# We are using write function to write lines and the input of characters is coming from list - For Loop
# We are using \n as it will separate the content of list into separate lines
# Than we are closing the file as it is already at the end of the file & we do not want anyone else to update the file
# Also, we have to close the file because we cannot read the content from the end of the file
# Alternate of this would be to go to start of the file using seek function
# Reading the file content
# Reversing the list and reading the list by half of its length - len(list1)//2
# Swapping index[0] with index[-1] and so on
# list1[indexInc], list1[len(list1)-indexInc-1] = list1[len(list1)-indexInc-1], list1[indexInc]
# Printing list and writing the file again with reversed content stored in the list
# Reading it again

list1 = []
y = 0
x = 0

while y <= 5:
    x = input("Enter any value")
    list1.append(x)
    y = y + 1

print(list1)

fileReader = open('empFile.txt', 'w+')

for fileLines in list1:
    fileReader.write(fileLines + "\n")

fileReader.close()

fileReader = open('empFile.txt')

print(fileReader.read())

fileReader.close()

# Range takes first argument as starting index and 2nd argument as last index but if we have only one argument
# than last index - 1 is taken as the value
for indexInc in range(0, len(list1)//2):
    # This will swap first index value with last index value by using length of the
    list1[indexInc], list1[len(list1)-indexInc-1] = list1[len(list1)-indexInc-1], list1[indexInc]

print(list1)

fileReader = open('empFile.txt', 'w+')

for fileLines in list1:
    fileReader.write(fileLines + "\n")

fileReader.close()

fileReader = open('empFile.txt')

print(fileReader.read())

fileReader.close()
