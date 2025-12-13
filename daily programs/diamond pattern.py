n = int(input("Enter the number of rows (odd number for symmetry): "))
# Upper half of the diamond
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# Lower half of the diamond
for i in range(n - 1, 0, -1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()
