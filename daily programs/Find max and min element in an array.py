n = int(input("Enter number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

max_ele = arr[0]
min_ele = arr[0]

for ele in arr:
    if ele > max_ele:
        max_ele = ele
    if ele < min_ele:
        min_ele = ele

print("Maximum element:", max_ele)
print("Minimum element:", min_ele)
