sarr = [21, 10, 90, 233, 2, 81, 9, 29, 1, 40]
sarr.sort()
print(sarr)
target = 91

i = 0
for k in sarr:
	if target == k:
		print("Found in {}.".format(i))
		break
	elif target < k:
		print("Not found. Should be inserted at {}.".format(i))
		break
	i += 1
else:
	print(i)
