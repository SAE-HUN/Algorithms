n, m = map(int, input().split())

if n:
    H = [*map(int, input().split())]
else:
    H = []

sum_H = sum(H)+n
if sum_H>=m:
    print(0)
else:
    q, r = divmod(m-sum_H, len(H)+1)
    print((q*(q+1)*(2*q+1)//6)*(len(H)+1)+(q+1)**2*r)
