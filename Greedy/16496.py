def II():
    return int(input())

def MIS():
    return map(int, input().split())

def sort(arr):
    for i in range(0, len(arr)):
        index_min = i
        
        for j in range(i+1, len(arr)):
            if int(arr[index_min]+arr[j])<int(arr[j]+arr[index_min]):
                index_min = j
        
        arr[i], arr[index_min] = arr[index_min], arr[i]

n, zero_cnt = II(), 0
arr = input().split()
sort(arr)

print(0 if set(arr)=={'0'} else ''.join(arr))
