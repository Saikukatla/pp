n = int(input("Enter the length of the string: "))
s = input("Enter the string: ")
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char in s:
    if char_count[char] == 1:
        print("The first non-repeating character is:", char)
        break   
    else:
        print("There are no non-repeating characters.")

