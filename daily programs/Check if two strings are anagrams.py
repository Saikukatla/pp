n = input("Enter a string: ")
n1 = input("Enter a string: ")
if sorted(n) == sorted(n1):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")  