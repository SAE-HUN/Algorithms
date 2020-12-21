n = int(input())
negative, one, positive = [], [], []
zero = False
for i in range(n):
    num = int(input())
    if num <=0:
        if num < 0:
            negative.append(num)
        elif num == 0:
            zero = True
    elif num > 0:
        if num == 1:
            one.append(num)
        else:
            positive.append(num)
            
negative.sort()
positive.sort()
result = 0

if len(negative) % 2 != 0:
    if zero:
        negative.pop()
    else:
        result += negative.pop()
if len(positive) % 2 != 0:
    result += positive.pop(0)
result += len(one)

for i in range(len(negative)//2):
    result += negative[2*i] * negative[2*i+1]
for i in range(len(positive)//2):
    result += positive[2*i] * positive[2*i+1]
    
print(result)
