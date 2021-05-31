from bisect import bisect_left, bisect_right

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
_A = []
_B = []

for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += A[j]
        _A.append(tmp)

for i in range(m):
    tmp = 0
    for j in range(i, m):
        tmp += B[j]
        _B.append(tmp)

_A.sort()
_B.sort()
answer = 0

for i in range(len(_A)):
    answer += bisect_right(_B, t-_A[i])
    answer -= bisect_left(_B, t-_A[i])

print(answer)
