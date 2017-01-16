#!/usr/bin/python3

"""Returns the transcribed sequence of dnastring"""

dnastring = "ACGT"
rnastring = ""
for char in dnastring:
	if char == 'T':
		rnastring += 'U'
	else:
		rnastring += char
print("%s" %rnastring)
