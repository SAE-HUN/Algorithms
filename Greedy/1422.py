def sort(arr):
    for i in range(0, len(arr)):
        index_min = i
        
        for j in range(i+1, len(arr)):
            if int(arr[index_min]+arr[j])<int(arr[j]+arr[index_min]):
                index_min = j
        
        arr[i], arr[index_min] = arr[index_min], arr[i]

k, n = map(int, input().split())
max_num, arr = 0, []

for i in range(k):
    a = input().strip()
    arr.append(a)
    max_num = max(max_num, int(a))

arr.extend([str(max_num)]*(n-k)); sort(arr)
print(''.join(arr))
