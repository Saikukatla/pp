n = int(input("Enter the length : "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(input())
reversed_arr = arr[::-1]
print("Reversed array:", reversed_arr)
