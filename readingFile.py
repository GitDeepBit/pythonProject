fileVar = open('DummyTextFile.txt')

print(fileVar.read(4))
# Files are read by putting a cursor on the text inside the file and based on that cursor
# position it will take next characters from the file

print(fileVar.readline())
print(fileVar.readline())

print(fileVar.read(2))

print(fileVar.readline())

fileVar.close()

