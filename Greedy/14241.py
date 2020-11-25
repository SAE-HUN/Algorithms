input()
slimes = list(map(int, input().split()))

print((sum(slimes)**2 - sum(list(slime**2 for slime in slimes)))//2)
