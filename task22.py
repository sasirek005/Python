n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
result = []
for num in arr:
    if num >= 0:
        result.append(num)
for num in arr:
    if num < 0:
        result.append(num)
print("Rearranged array:")
print(result)
