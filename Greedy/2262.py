n = int(input())
ranks = list(map(int, input().split()))

answer = 0
while n>1:
    idx = ranks.index(n)
    min_rank = ranks[idx]
    left = ranks[idx-1] if idx>0 else 0
    right = ranks[idx+1] if idx<n-1 else 0
    
    answer += min_rank - max(left, right)
    del ranks[idx]
    n -= 1

print(answer)
