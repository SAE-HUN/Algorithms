while True:
    n, a, b = map(int, input().split())
    
    if n==0:
        break
    
    teams = [tuple(map(int, input().split())) for _ in range(n)]
    teams.sort(key=lambda x:abs(x[1]-x[2]), reverse=True)
    answer = 0
    
    for k, da, db in teams:
        if da>=db:
            num = min(k, b)
            answer += db*num
            k -= num
            b -= num
            
            answer += da*k
            a -= k
        else:
            num = min(k, a)
            answer += da*num
            k -= num
            a -= num
            
            answer += db*k
            b -= k
    
    print(answer)
