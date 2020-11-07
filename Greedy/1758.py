def get_tip(num):
    return max(tips[i] - i, 0)

n = int(input())
tips = [int(input()) for _ in range(n)]

tips.sort(reverse=True)
answer = 0
for i in range(n):
    tip = get_tip(i)
    answer += tip
    
print(answer)
