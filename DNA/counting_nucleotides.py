#!/usr/bin/python3

ntdict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
ntstring = "ACGT"
for char in ntstring:
	ntdict[char] += 1
countlist = []
for key in sorted(ntdict):
	countlist.append(str(ntdict[key]))
printable = ' '.join(countlist)
print("%s" %printable)
