n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
result = []
for num in arr:
    if num != 0:
        result.append(num)
while len(result) < n:
    result.append(0)
print("Array after moving zeros to the end:")
print(result)
