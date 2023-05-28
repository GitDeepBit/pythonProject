# TRY block will consist of code which has potential of failing & it will raise exception
# EXCEPT block will help us run code, when exception is raised by TRY block

# When the code inside TRY block returns true, meaning it works
# It will not go to EXCEPT block

# TRY and EXCEPT are used to handle such errors which are unexpected ( where we have uncertainty )
# AND we want the code to run, even after such unexpected errors ( exceptions )

try:
    with open("ABCDEFG.txt", 'r') as fileReader:
        fileReader.read()

except:
    print("File is not present, creating new file here")
    with open("ABCDHIJAA.txt", 'a+') as fileReader1:
        print("New file is created which is named as:", fileReader1.name)
        fileReader1.read()

