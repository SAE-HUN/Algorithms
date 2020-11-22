n = int(input())
books = []

for i in range(n):
    book = int(input().strip())
    books.append(book)
    
    if book==n:
        n_idx = i

answer, next_book = n-1, n-1
for book in reversed(books[:n_idx]):
    if book==next_book:
        answer -= 1
        next_book -= 1

print(answer)
