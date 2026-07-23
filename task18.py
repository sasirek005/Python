n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
found = False
print("Triplets are:")
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] == 0:
                print(arr[i], arr[j], arr[k])
                found = True
if not found:
    print("No triplets found")
