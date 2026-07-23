n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
largest = second_largest = float('-inf')
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
if second_largest == float('-inf'):
    print("Second largest element does not exist.")
else:
    print("Second largest element is:", second_largest)
