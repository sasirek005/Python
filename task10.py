n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
print("Array elements in reverse order:")

for i in range(n - 1, -1, -1):
    print(arr[i], end=" ")
