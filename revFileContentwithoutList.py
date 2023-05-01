# Here we will read the file content and store it inside the list and then reverse it
# and write that reverse content inside the file. But here we are using reversed function instead of swap logic

# byte == index in case of files
with open('empFile.txt', 'r+') as fileReader:
    list1 = fileReader.readlines()
    fileReader.seek(0)
    for fileLines in reversed(list1):
        fileReader.write(fileLines)
    fileReader.seek(0)  # This will send the file pointer to the desired byte of the file "in this case first byte"
    print(fileReader.read())
