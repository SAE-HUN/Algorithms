import sys
input = sys.stdin.readline

n = int(input())
words = set()

for _ in range(n):
    word = input()
    words.add(word)

words = list(words)
words.sort()
words.sort(key=lambda x: len(x))
print(''.join(words))
