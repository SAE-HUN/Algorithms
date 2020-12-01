t = int(input())
arr = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]

for _ in range(t):
    n = int(input())
    ans2 = '7'*(n%2)+'1'*(n//2-n%2)
    
    if n<=10:
        ans1 = arr[n]
    else:
        ans1 = '8'*(n//7); n %= 7
        brr = {6:'6', 2:'1', 5:'2'}
        
        if n in brr:
            ans1 = brr[n]+ans1
        else:
            crr = {1:'10', 4:'20'}
            if n in crr:
                ans1 = crr[n]+ans1[1:]
            elif n==3:
                ans1 = '200'+ans1[2:]
    
    print(ans1, ans2)
