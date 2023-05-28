# Raising python generated Exception using except Exception as "Variable" and printing it in line 8

try:
    with open("ABCDEFG.txt", 'r') as fileReader:
        fileReader.read()

except Exception as exception_error:
    print(exception_error)
    with open("ABCDHIJAA.txt", 'a+') as fileReader1:
        print("New file is created and it is named as:", fileReader1.name)

finally:
    print("This block is a finally block and this will run, no matter Try is failed or not")
    with open('empFile.txt', 'r') as fileReader2:
        print(fileReader2.read())

