# Open function is used to open the file and argument will be the path/Name of the text file

# We created new object as for the file

fileobj = open("DummyTextFile.txt")
fileobj1 = open("DummyFile2.txt")

# Read function is used to read the file content & it reads all the content at one go
# Once the content is read by this function, cursor on the file moves to the end of the file
print(fileobj.read())

# If we pass numerical argument inside the read function, it will treat the argument as number of bytes
# Here bytes is referred to the number of character. So, the below output will read 5 characters ( including /n )
print(fileobj1.read(5))
# Always close the file, so that no information is leaked OR it is not overridden by any piece of code later on

# Here the content was already read till 5th character in the file due to line code 14
# And for that reason it started reading lines from next character and printed "ontent"
print(fileobj1.readline())

# And this will print next line, that space between two lines in between two readlines is "Enter" or /n
print(fileobj1.readline())

# And this will print next line and so on
print(fileobj1.readline())

print(fileobj1.read(3))

print(fileobj1.readline())

fileobj.close()
fileobj1.close()
