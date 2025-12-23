n = input("Enter a string: ")
result = ""
for char in n:  
    if char not in result:
        result += char  
print("String after removing duplicate characters:", result)    
    