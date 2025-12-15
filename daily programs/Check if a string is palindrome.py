n = input("Enter a string: ")
l = 0
r = len(n) - 1
is_palindrome = True
while l < r:
    if n[l] != n[r]:
        is_palindrome = False
        break
    l += 1
    r -= 1
if is_palindrome:
    print("palindrome") 
else:
    print("not a palindrome")