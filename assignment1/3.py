from itertools import zip_longest

a = "1100" # 12
b =  "101" # 5

print(a)

carry = False
c = ""
for i, k in zip_longest(a[::-1], b[::-1], fillvalue="0"):
	if carry:
		res = int(i) + int(k) + 1
	else:
		res = int(i) + int(k)
	if res == 2:
		c = "0" + c
		carry = True
	else:
		c = str(res) + c
		carry = False
else:
	if carry:
		c = "1" + c

print(c)
print(int(c, 2))
