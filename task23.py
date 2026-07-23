n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
found = False
for i in range(n):
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i+1:])
    if left_sum == right_sum:
        print("Equilibrium index:", i)
        found = True
        break
if not found:
    print("No equilibrium index found")
