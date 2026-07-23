n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
smallest = arr[0]
for i in range(1, n):
    if arr[i] < smallest:
        smallest = arr[i]
print("Smallest element is:", smallest)
