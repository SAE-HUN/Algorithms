def dfs(string, button):
    string += str(button)
    channels.append(int(string))
    
    if len(string)==6:
        return
    
    for button in buttons:
        dfs(string, button)

def get_cnt(channel):
    return len(str(channel))+abs(n-channel)

n, m = int(input()), int(input())
buttons = [i for i in range(10)]

try:
    for button in map(int, input().split()):
        buttons.remove(button)
except:
    pass

channels = []
for button in buttons:
    dfs('', button)

channels = list(set(channels))
channels.sort(key=get_cnt)

print(min(abs(n-100), get_cnt(channels[0])) if channels else abs(n-100))
