def update_truck(dispatch, destination, box):
	for i in range(dispatch, destination):
		truck[i] -= box

n, c = map(int, input().split())
m = int(input())
deliveries = [tuple(map(int, input().split())) for _ in range(m)]
deliveries.sort(key=lambda x: x[1])
truck = [c] * (n+1)
answer = 0

for dispatch, destination, box in deliveries:
	available_box = min(truck[dispatch:destination])
	if available_box == 0:
		continue
	if available_box > box:
		loaded_box = box
	else:
		loaded_box = available_box
	answer += loaded_box
	update_truck(dispatch, destination, loaded_box)
	
print(answer)
