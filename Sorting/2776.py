t = int(input())
while t:
    t -= 1
    n = int(input())
    first_note = list(map(int, input().split()))
    m = int(input())
    second_note = list(map(int, input().split()))
    first_note.sort()
    
    def binary_search(x):
        l = 0
        r = n
        
        while l<r:
            mid = (l+r)//2
            if first_note[mid]<x:
                l = mid + 1
            else:
                r = mid
        
        try:
            return int(first_note[l]==x)
        except:
            return 0
    
    for x in second_note:
        print(binary_search(x))
