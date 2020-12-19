def get_not_zero(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i]!='0':
            return arr.pop(i)

while True:
    case = input().split()
    n = case[0]
    arr = sorted(case[1:], reverse=True)
    
    if n=='0':
        break
    
    a = get_not_zero(arr)
    b = get_not_zero(arr)
    
    while True:
        try:
            a += arr.pop()
            b += arr.pop()
        except:
            break
    
    print(int(a)+int(b))
