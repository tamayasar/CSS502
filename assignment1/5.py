from collections import Counter

dna = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
substrings = []

last = len(dna) - 10

for i in range(last + 1):
	substrings.append(dna[i:i+10])

occ = Counter(substrings)
print([x for x in occ if occ[x] == 2])
