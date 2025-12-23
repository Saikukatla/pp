n = int(input("Enter number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

largest = arr[0]
second_largest = -1

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i
    elif i != largest and i > second_largest:
        second_largest = i

print("Second largest element:", second_largest)
