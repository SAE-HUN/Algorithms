import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())*10**7
    except:
        exit()
    
    n = int(input())
    lego = [int(input()) for _ in range(n)]
    lego.sort()
    
    answer = ['danger']
    l = 0
    r = n-1
    
    while l<r:
        s = lego[l]+lego[r]
        
        if s<x:
            l += 1
        elif s>x:
            r -= 1
        else:
            answer = ['yes', lego[l], lego[r]]
            break
    
    print(*answer)
