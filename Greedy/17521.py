n, w = map(int, input().split())
prices = [0]

for _ in range(n):
    price = int(input())
    if price==prices[-1]:
        continue
    prices.append(price)
del prices[0]

buy_point = []
if len(prices)>1 and prices[1]>prices[0]:
    buy_point.append(0)

for i in range(1, len(prices)-1):
    if prices[i]<prices[i-1] and prices[i]<prices[i+1]:
        buy_point.append(i)

if buy_point:
    for i in range(len(buy_point)-1):
        buy_price = prices[buy_point[i]]
        num = w//buy_price
        w %= buy_price
        w += num*max(prices[buy_point[i]:buy_point[i+1]])
    
    buy_price = prices[buy_point[-1]]
    num = w//buy_price
    w %= buy_price
    w += num*max(prices[buy_point[-1]:])

print(w)
