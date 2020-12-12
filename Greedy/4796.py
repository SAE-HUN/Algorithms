num = 1
while(True):
    l, p, v = map(int, input().split())
    if l == 0:
        break
    result = v//p*l + min(l, v%p)
    print(f'Case {num}: {result}')
    num += 1
