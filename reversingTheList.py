# Taking inputs from user and inserting the values in an empty List
# Printing the output of the list - To check
# Opening the file in write mode and writing the lines using w+ feature
# We are using write function to write lines and the input of characters is coming from list - For Loop
# We are using \n as it will separate the content of list into separate lines
# Than we are closing the file as it is already at the end of the file & we do not want anyone else to update the file
# Also, we have to close the file because we cannot read the content from the end of the file
# Alternate of this would be to go to start of the file using seek function
# Reading the file content
# Reversing the list using 2nd List by starting from end of the list to start of the list
# range(len(list1) - 1, -1, -1)
# len(list1) -1 meaning starting from the end of the list
# -1, -1 meaning till the end of list by decrementing the index by -1
# Appending list2 with list1 - list2.append(list1[indexInc])
# Printing list and writing the file again with reversed content stored in the list
# Reading it again

list1 = []
list2 = []
y = 0
x = 0

while y <= 5:
    i = input("Enter any value ")
    list1.append(i)
    y = y + 1

print(list1)

fileReader = open('empFile.txt', 'w+')

for fileLines in list1:
    fileReader.write(fileLines + "\n")

fileReader.close()

fileReader = open('empFile.txt')

print(fileReader.read())

fileReader.close()

for indexInc in range(len(list1) - 1, -1, -1):
    # list2.insert(x, indexInc)
    # x += 1
    list2.append(list1[indexInc])

list1 = list2

print(list1)

# When we open file in w+ mode it will clear the contents of the file and starting writing from first index
fileReader = open('empFile.txt', 'w+')

for fileLines in list1:
    fileReader.write(fileLines + "\n")

fileReader.close()

fileReader = open('empFile.txt')

print(fileReader.read())

fileReader.close()



