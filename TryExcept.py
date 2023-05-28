
try:
    with open("ABC.txt") as r1:
        r1.read()

except:
    print("Cannot open the file")

try:
    with open("ABC.txt") as r1:
        r1.read()

except Exception as exc:
    print(exc)

finally:
    print("Chalo Shukkar hai, mein toh chalunga")

