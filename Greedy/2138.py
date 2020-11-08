def solution(current, push_first=False):
    def change_state(i):
        current[i] = 1 - current[i]

    def push(i):
        for j in range(-1, 2):
            if i+j<0 or i+j>=n:
                continue
            change_state(i+j)

    count = 0
    
    if push_first:
        count += 1
        push(0)

    for i in range(1, n):
        if current[i-1] != wanted[i-1]:
            count += 1
            push(i)

    if current == wanted:
        return count
    else:
        return n+1

n = int(input())
current = list(map(int, list(input().strip())))
wanted = list(map(int, list(input().strip())))

answer = min(solution(current[:]), solution(current[:], True))
if answer == n+1:
    print(-1)
else:
    print(answer)
