# Here we will read the file content and store it inside the list and then reverse it
# and then write that reverse content of the list inside the file

# byte == index in case of files
with open('empFile.txt', 'r') as fileReader:
    list1 = fileReader.readlines()  # This reaches end of the file
    fileReader.seek(0)  # This will send the file pointer to the desired byte of the file "in this case first byte"
    print(fileReader.read())


# \n is taken as a character inside the list but file takes it as a next line
# The list created here is actually created through readlines which is making the list in the below format
# ['6\n', '5\n', '4\n', '3\n', '2\n', '1\n']
# If we append one more \n while writing the lines in fileReader.write(fileLines + "\n")
# It will append one more new blank line as it takes \n as next line character and "not a character part of the string"
print(list1)


# Range takes first argument as starting index and 2nd argument as last index but if we have only one argument
# than last index - 1 is taken as the value
for indexInc in range(0, len(list1)//2):
    # This will swap first index value with last index value by using length of the
    list1[indexInc], list1[len(list1)-indexInc-1] = list1[len(list1)-indexInc-1], list1[indexInc]


with open('empFile.txt', 'w+') as fileReader:
    for fileLines in list1:
        fileReader.write(fileLines)
    fileReader.seek(0)
    print(fileReader.read())
