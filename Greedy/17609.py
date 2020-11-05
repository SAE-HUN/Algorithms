def skip(l, r):
	while l<=r:
		if s[l]!=s[r]:
			return 2
		l += 1
		r -= 1
	return 1

t = int(input())

for _ in range(t):
	s = input()
	answer = 0
	l = 0
	r = len(s)-1

	while l<=r:
		if s[l]!=s[r]:
			if answer:
				answer = 2
				break
			else:
				answer = 1
				if s[l+1]==s[r] and s[l]==s[r-1]:
					answer = min(skip(l+1, r), skip(l, r-1))
					break
				elif s[l+1]==s[r]:
					l += 1
				elif s[l]==s[r-1]:
					r -= 1
				else:
					answer = 2
					break
		else:
			l += 1
			r -= 1

	print(answer)
