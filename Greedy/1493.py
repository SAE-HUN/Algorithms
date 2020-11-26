l, w, h = map(int, input().split())
n = int(input())
cubes = [0]*20

for _ in range(n):
    i, mnt = map(int, input().split())
    cubes[i] = mnt

answer, prev = 0, 0

for i in range(19, -1, -1):
    prev <<= 3
    possible = (l >> i) * (w >> i) * (h >> i) - prev
    new = min(cubes[i], possible)
    answer += new
    prev += new

print(answer if prev==l*w*h else -1)
