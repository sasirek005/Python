n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
k = int(input("Enter the value of K: "))
found = False
for i in range(n):
    for j in range(i + 1, n):
        if abs(arr[i] - arr[j]) == k:
            print("Pair found:", arr[i], arr[j])
            found = True
            break
    if found:
        break
if not found:
    print("No pair found")
