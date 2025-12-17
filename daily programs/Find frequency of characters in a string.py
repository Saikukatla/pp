n = input("Enter a string: ")
freq = {}
for char in n:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1  
for char, count in freq.items():
    print(f"'{char}': {count}")
