n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
print("Leaders are:")
max_right = arr[n - 1]
print(max_right)
for i in range(n - 2, -1, -1):
    if arr[i] > max_right:
        max_right = arr[i]
        print(max_right)
