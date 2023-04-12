str1, str2, str3 = "First.String.Continued", "Second String", "String"

print(str1[2])  # Index value from string

print(str2[0:5])  # Range of values

print(str1 + " " + str2 + " " + str3)  # Concatenation

print(str3 in str1)  # Finding string value in another string, subset. Returns True or False

split1 = str1.split("i", 3)  # Splits the string based on the character given as argument in split
print(split1)

print(str1)

str4 = " great  string "  # Strips the white spaces from the beginning and end of the string
print(str4.strip())
print(str4)


