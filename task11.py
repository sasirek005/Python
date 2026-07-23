n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
print("
found = False
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            print(arr[i])
            found = True
            break
if not found:
    print("No duplicate elements")
