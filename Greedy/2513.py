n, k, s = map(int, input().split())
left, right = [], []

for _ in range(n):
    apt, stu = map(int, input().split())
    
    if apt<s:
        left.append((s-apt, stu))
    else:
        right.append((apt-s, stu))

left.sort()
right.sort()

answer= 0

while left:
    bus = k
    answer += 2*left[-1][0]
    
    while bus>0 and left:
        apt, stu = left.pop()
        num = min(bus, stu)
        bus -= num
        stu -= num
        
        if stu>0:
            left.append((apt, stu))

while right:
    bus = k
    answer += 2*right[-1][0]
    
    while bus>0 and right:
        apt, stu = right.pop()
        num = min(bus, stu)
        bus -= num
        stu -= num
        
        if stu>0:
            right.append((apt, stu))

print(answer)
