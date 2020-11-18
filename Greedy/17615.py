n = int(input())
balls = list(input())

answer = n
try:
    r_first = balls.index('R')
    b_first = balls.index('B')
    
    answer = min(answer, balls[r_first:].count('B'), balls[b_first:].count('R'))
    
    balls.reverse()
    r_first = balls.index('R')
    b_first = balls.index('B')
    
    answer = min(answer, balls[r_first:].count('B'), balls[b_first:].count('R'))
except:
    print(0)
    exit()

print(answer)
