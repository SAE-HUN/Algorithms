import sys

t = int(input())

while t:
    t -= 1
    n = int(input())
    numbers = []
    
    for _ in range(n):
        number = sys.stdin.readline().rstrip()
        numbers.append(number)
    
    numbers.sort(key=lambda x: (x, len(x)))
    answer = 'YES'
    
    for i in range(1, n):
        prev = numbers[i-1]
        now = numbers[i]
        
        if now.startswith(prev):
            answer = 'NO'
            break
    
    print(answer)
