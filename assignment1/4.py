arr = [32, 2, 9, 12, 2, 0, 0, 99, 32, 9, 99]
tracker = []

for i in arr:
	if i in tracker:
		tracker.remove(i)
	else:
		tracker.append(i)

print(tracker[0])
