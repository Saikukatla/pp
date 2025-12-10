n = int(input("Enter a number: "))
original_n = n
reversed_n = 0
while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n //= 10
if original_n == reversed_n:
    print(f"{original_n} is a palindrome.")
else:
    print(f"{original_n} is not a palindrome.")
