n = int(input()); ss, k = [input().strip() for _ in range(n)], int(input())
scores = {i:0 for i in range(36)}

for s in ss:
    for i, num in enumerate(s):
        if ord(num)>=65:
            num = ord(num)-55
        else:
            num = int(num)
        
        scores[num] += 36**(len(s)-i-1)

z, scores = [], sorted(list(scores.items()), reverse=True, key=lambda x:x[1]*(35-x[0]))
for num, score in scores[:k]:
    if num<10:
        z.append(str(num))
    else:
        z.append(chr(num+55))

answer10 = 0
for s in ss:
    for i, num in enumerate(s):
        if num in z:
            num = 'Z'
        
        if ord(num)>=65:
            num = ord(num)-55
        else:
            num = int(num)
        
        answer10 += num*(36**(len(s)-i-1))

def toThree(num):
    if num<10:
        return str(num)
    else:
        return chr(num-10+65)

answer36=""
while(answer10//36):
    remain=toThree(answer10%36)
    answer36=remain+answer36
    answer10=answer10//36
answer36=toThree(answer10)+answer36

print(answer36)
