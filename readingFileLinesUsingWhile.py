fileVar = open('DummyTextFile.txt')

line = fileVar.readline()

while line != "":
    print(line)
    line = fileVar.readline()

fileVar.close()

