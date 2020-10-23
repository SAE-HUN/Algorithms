sentence = list(input())

try:
	U = sentence.index("U")
	try:
		C = sentence[U+1:].index("C")
		try:
			P = sentence[U+C+2:].index("P")
			try:
				C = sentence[U+C+P+3:].index("C")
				answer = 'I love UCPC'
			except:
				answer = 'I hate UCPC'
		except:
			answer = 'I hate UCPC'
	except:
		answer = 'I hate UCPC'
except:
	answer = 'I hate UCPC'

print(answer)