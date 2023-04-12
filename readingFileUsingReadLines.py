fileVar = open('DummyTextFile.txt')

# lineLists = fileVar.readlines()  # if we do this than it will take first line and readlines will increment it
# print(lineLists[0])  Readlines will read all the lines at once and cannot be used further for reading purpose

for lines in fileVar.readlines():
    print(lines)

fileVar.close()