n, note = int(input()), [*map(int, input().split())]
answer, buttons = 0, [0]*n

for i in range(n):
    if buttons[i]!=note[i]:
        answer += 1
        try:
            buttons[i] = -buttons[i]+1
            buttons[i+1] = -buttons[i+1]+1
            buttons[i+2] = -buttons[i+2] + 1
        except:
            pass

print(answer)
