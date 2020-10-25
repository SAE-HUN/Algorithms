import heapq
import sys

n = int(sys.stdin.readline().strip())
timetable = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
timetable.sort(key=lambda x: (x[0], x[1]))
heapq.heapify(timetable)
rooms = [0]

for i in range(n):
	s, t = heapq.heappop(timetable)
	end = heapq.heappop(rooms)
	if end <= s:
		heapq.heappush(rooms, t)
	else:
		heapq.heappush(rooms, end)
		heapq.heappush(rooms, t)
	
print(len(rooms))
