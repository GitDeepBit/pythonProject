fileVar = open('DummyTextFile.txt')

# lineLists = fileVar.readlines()  # if we do this than it will take first line and readlines will increment it
# print(lineLists[0])  Readlines will read all the lines at once and cannot be used further for reading purpose

for lines in fileVar.readlines():
    print(lines)

fileVar.close()

# If we used readLines(), output of the file will be separated with new lines in between
# but if we use read(), it will show the output in normal format i.e. without new line gap

