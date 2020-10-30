n = int(input())
seats = list(input())
answer = 1
flag = 0
for seat in seats:
    if seat == 'S':
        answer += 1
    elif seat == 'L':
        if flag == 0:
            flag = 1
        elif flag == 1:
            answer += 1
            flag = 0
print(min(answer, n))
