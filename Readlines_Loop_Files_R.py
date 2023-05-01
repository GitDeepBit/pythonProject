fileObj = open("DummyTextFile.txt")
fileObj1 = open("DummyFile2.txt")

lineObj = fileObj.readline()

while lineObj != "":
    print(lineObj)
    # If we do not perform the next step, it will become infinite loop
    # How? Well, ABC is the first line & it is not equal to "Blank" and we are not changing the line variable's value
    # So, it will run infinitely. To change the content we will shift the curso from first line to second line
    # USING readline
    # Now the below code will shift the cursor to next line & it will read it
    lineObj = fileObj.readline()

# This will store the lines in a list
lineObj1 = fileObj1.readlines()

# This will print the output in a list
print(lineObj1)

# Reading the list using for loop by interation of index
for line in lineObj1:
    print(line)

fileObj.close()
fileObj1.close()