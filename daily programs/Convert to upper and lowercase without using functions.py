n = input("Enter a string: ")
upper_case = ""
lower_case = ""
for char in n:
    if 'a' <= char <= 'z':
        upper_case += chr(ord(char) - 32)
        lower_case += char
    elif 'A' <= char <= 'Z':
        lower_case += chr(ord(char) + 32)
        upper_case += char
    else:
        upper_case += char
        lower_case += char
print("Uppercase:", upper_case)
print("Lowercase:", lower_case)
