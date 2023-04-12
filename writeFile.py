with open('DummyTextFile.txt', 'r') as read1:
    content = read1.readlines()
    fileContentR = reversed(content)
    with open('DummyTextFile.txt', 'w') as w1:
        for lines in fileContentR:
            w1.write(lines)
            print(lines)
    # print(fileContentR)