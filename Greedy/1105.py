l, r = input().split()

if l==r:
    answer = l.count('8')
else:
    answer = 0
    if len(l)==len(r):
        for i in range(len(l)):
            if l[i]!=r[i]:
                break
            if l[i]=='8':
                answer += 1

print(answer)
