# Here we will read the file content and store it inside the list and then reverse it
# and write that reverse content inside the file. But here we are using "reversed" function instead of swap logic

# Definition of with
# The with statement works with the open() function to open a file.
# Unlike open() where you have to close the file with the close() method,
# the with statement closes the file for you without telling you.
# This is because the with statement calls 2 built-in methods behind the scene – __enter()__ and __exit()__

# byte == index in case of files
with open('empFile.txt', 'r+') as fileReader:
    list1 = fileReader.readlines()  # reads file content in one-go and stores the value in form of list
    fileReader.seek(0)  # sends back the index of the filereader to first index
    for fileLines in reversed(list1):  # fetching the data from a reversed list content
        fileReader.write(fileLines)  # writing the content back to the file
    fileReader.seek(0)  # This will send the file pointer to the desired byte of the file "in this case first byte"
    print(fileReader.read())

# automatically file closes
