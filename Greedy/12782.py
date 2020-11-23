t = int(input())

for _ in range(t):
    a, b = input().split()
    diff = 0
    
    for i in range(len(a)):
        if a[i]!=b[i]:
            diff += 1
    
    a_zero = a.count('0')
    b_zero = b.count('0')
    zero_diff = abs(a_zero-b_zero)
    
    print((diff-zero_diff)//2 + zero_diff)
