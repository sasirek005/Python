n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
total = 0
for num in arr:
    total += num
average = total / n
print("Average of array elements is:", average)
