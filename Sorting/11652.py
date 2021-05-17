import sys
from collections import Counter

n = int(input())
cards = list(map(int, sys.stdin.read().splitlines()))
print(sorted(Counter(cards).most_common(), key=lambda x: (-x[1], x[0]))[0][0])
