import sys

def II():
    return int(sys.stdin.readline().strip())

def MIS():
    return map(int, sys.stdin.readline().split())

n = II()
X, P = [], []
money, a, b = 0, 0, False

for i in range(n):
    x, p = MIS()
    P.append(p)
    X.append(x)
    
    if money>x:
        if not b:
            b = i
        a = max(a, money-x)
    
    money += p

if not a or b==n-1:
    print('Kkeo-eok')
    exit()

money = 0

for i in range(b):
    money += P[i]
    
    if P[i]>=a:
        print('Kkeo-eok')
        exit()

flag = 1

for i in range(b+1, n):
    if money>X[i]:
        flag = 0
        break
    money += P[i]

print('Kkeo-eok' if flag else 'Zzz')
