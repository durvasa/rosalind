#!/usr/bin/python3

""" Returns the reverse complement of dnastring"""

complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
dnastring = "ACGT"
reversed_complement = ""

reversed_dnastring = dnastring[::-1]
for char in reversed_dnastring:
	reversed_complement += complement[char]

print("%s" %reversed_complement)
