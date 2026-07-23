n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
target = int(input("Enter the required sum: "))
found = False
for i in range(n):
    total = 0
    for j in range(i, n):
        total += arr[j]
        if total == target:
            print("Subarray:", arr[i:j+1])
            found = True
            break
    if found:
        break
if not found:
    print("No subarray found")
