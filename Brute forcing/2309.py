import sys

dwarfs = [*map(int, sys.stdin.read().split())]
sum_tall = sum(dwarfs)

for i in range(8):
    for j in range(i+1, 9):
        if dwarfs[i]+dwarfs[j]==sum_tall-100:
            del dwarfs[i]; del dwarfs[j-1]
            for tall in sorted(dwarfs):
                print(tall)
            exit()
