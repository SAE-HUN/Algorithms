n = int(input())

periods = []
months = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

for _ in range(n):
    on_m, on_d, off_m, off_d = map(int, input().split())
    on = months[on_m]+on_d
    off = months[off_m]+off_d
    periods.append((on, off))

periods.sort()
i, answer, temp, maginot = -1, 0, 0, months[3]+1

while i<n and maginot<=months[12]:
    i += 1
    flag = 0
    
    for j in range(i, n):
        on, off = periods[j][0], periods[j][1]
        if on>maginot:
            break
        
        if off>temp:
            flag = 1
            temp = off
            i = j
    
    if flag:
        answer += 1
        maginot = temp
    else:
        answer = 0
        break

print(answer)
