n = int(input())
k = int(input())
sensors = sorted(set(list(map(int, input().split()))))

intervals = []
for i in range(len(sensors)-1):
	interval = sensors[i+1] - sensors[i]
	intervals.append((interval, i))
intervals.sort(reverse=True)

answer = 0
if k == 1:
	answer += sensors[-1] - sensors[0]
elif len(intervals) >= k-1:
	intervals = intervals[:k-1]
	intervals.sort(key=lambda x:x[1])
	
	answer += sensors[intervals[0][1]] - sensors[0]
	for i in range(1, len(intervals)):
		answer += sensors[intervals[i][1]] - sensors[intervals[i-1][1]+1]
	answer += sensors[-1] - sensors[intervals[-1][1]+1]
		
print(answer)
