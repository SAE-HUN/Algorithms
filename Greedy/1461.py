def solution(idx, books):
    global answer
    while idx < len(books):
        answer += 2*books[idx]
        idx += m

n, m = map(int, input().split())
books = list(map(int, input().split()))

neg_books = []
pos_books = []
for book in books:
    if book < 0:
        neg_books.append(-book)
    else:
        pos_books.append(book)

answer = 0
neg_books.sort(reverse=True)
pos_books.sort(reverse=True)

solution(0, neg_books)
solution(0, pos_books)

if neg_books and pos_books:
    answer -= max(neg_books[0], pos_books[0])
elif neg_books:
    answer -= neg_books[0]
else:
    answer -= pos_books[0]

print(answer)
