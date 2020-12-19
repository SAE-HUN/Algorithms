def II():
    return int(input())

def MIS():
    return map(int, input().split())

def factorizate(n):
    primes = [2, 3, 5, 7]
    cnt = [0, 0, 0, 0]
    
    for i, prime in enumerate(primes):
        if n%prime==0:
            while n%prime==0:
                cnt[i] += 1
                n //= prime
    
    return n, cnt

t = II()

for _ in range(t):
    n = II()
    
    if n==1:
        print(1)
        continue
    
    n, cnt = factorizate(n)
    
    if n!=1:
        print(-1)
        continue
    
    answer = ['8']*(cnt[0]//3)
    cnt[0] %= 3
    answer.extend(['4']*(cnt[0]//2))
    cnt[0] %= 2
    answer.extend(['9']*(cnt[1]//2))
    cnt[1] %= 2
    a = min(cnt[0], cnt[1])
    answer.extend(['6']*a)
    cnt[0] -= a
    cnt[1] -= a
    answer.extend(['5']*cnt[2])
    answer.extend(['7']*cnt[3])
    answer.extend(['2']*cnt[0])
    answer.extend(['3']*cnt[1])
    answer.sort()
    
    print(len(''.join(answer)))
