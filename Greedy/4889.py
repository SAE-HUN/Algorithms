n = 1

while True:
    s = input().strip()
    if s[0]=='-':
        break
    
    _open = 0
    answer = 0
    for i in range(len(s)):
        if s[i]=='{':
            _open += 1
        else:
            if _open>0:
                _open -= 1
            else:
                answer += 1
                _open += 1
    
    answer += _open//2
    print(str(n) + '. ' + str(answer))
    n += 1
