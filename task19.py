n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
majority = None
for i in range(n):
    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count += 1
    if count > n // 2:
        majority = arr[i]
        break
if majority is not None:
    print("Majority element is:", majority)
else:
    print("No majority element")
