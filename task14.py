n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
max_len = 1
curr_len = 1
start = 0
end = 0
temp = 0
for i in range(1, n):
    if arr[i] > arr[i - 1]:
        curr_len += 1
    else:
        curr_len = 1
        temp = i
    if curr_len > max_len:
        max_len = curr_len
        start = temp
        end = i
print("Longest increasing subarray:", arr[start:end+1])
