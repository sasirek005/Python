n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

target = int(input("Enter the required sum: "))
found = False
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            print("Pair found:", arr[i], arr[j])
            found = True
            break
    if found:
        break
if not found:
    print("No pair found")
