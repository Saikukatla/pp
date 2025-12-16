n = input("Enter a string: ")
vowels = "aeiouAEIOU"
no_vowel_string = ""        
for char in n:
    if char not in vowels:
        no_vowel_string += char 
print("String without vowels:", no_vowel_string)