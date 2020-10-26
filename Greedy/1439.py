s = list(input())
zero = 0
one = 0

if s[0] == '0':
	flag = '0'
	zero += 1
else:
	flag = '1'
	one += 1

for i in s:
	if i != flag:
		if flag == '0':
			one += 1
			flag = '1'
		else:
			zero += 1
			flag = '0'
			
print(min(zero, one))
