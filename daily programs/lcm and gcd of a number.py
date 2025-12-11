a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Save original values
x, y = a, b

# Find GCD
while b != 0:
    a, b = b, a % b

gcd = a
lcm = (x * y) // gcd

print("GCD =", gcd)
print("LCM =", lcm)
