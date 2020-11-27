n = int(input())
dice = list(map(int, input().split()))

if n==1:
    _max, _sum = 0, 0
    
    for num in dice:
        _sum += num
        _max = max(_max, num)
    
    print(_sum-_max)
else:
    min_1, min_2, min_3 = 50, 100, 150
    
    for i in range(6):
        min_1 = min(min_1, dice[i])
        
        for j in range(i+1, 6):
            if i+j==5:
                continue
            
            min_2 = min(min_2, dice[i]+dice[j])
            
            for k in range(j+1, 6):
                if i+k==5 or j+k==5:
                    continue
                
                min_3 = min(min_3, dice[i]+dice[j]+dice[k])
    
    mnt_1 = 5*(n**2) - 16*n + 12
    mnt_2 = 8*n - 12
    mnt_3 = 4
    
    print(min_1*mnt_1 + min_2*mnt_2 + min_3*mnt_3)
