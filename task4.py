n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
smallest = second_smallest = float('inf')
for num in arr:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
if second_smallest == float('inf'):
    print("Second smallest element does not exist.")
else:
    print("Second smallest element is:", second_smallest)
