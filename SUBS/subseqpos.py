#!/usr/bin/python3

""" Provides the indexes of all occurrence of subseq within seq"""

seq = "AGGGATAAGTTCGGGATAACCTTAGGTAGGGATAAAGGGATAAGCAGTCATTGGGATAAGGGGATAACCTTTTACAGGGATAAGAACGGGATAAACCAGGGATAAACAGCGCAGGGATAACTATAGGGGATAATCTGGGATAATGGGATAATGGGATAAGGGATAAGGGGATAAATAGTGGGATAAACAATTCCGCACGGGATAAAGGGATAAGGGATAAACGGGATAAGGGATAAGGGATAAACGGGATAAGGGATAAGCTGGGATAAGCAGGGGGATAATCGGGGATAAGGGGATAACTGGGATAAGAATTCGGGGATAATTTGGGATAAGGGATAAGGGATAAAGACAAGAATTGGGATAAGGGATAATTAAACCTGGGATAACTGTTCGGGATAACTGGAAGGAATAAGGGATAATGGGGGGATAAGGGATAAGGGGATAAGGGATAAGGGATAATCTGGGGATAAGGGATAAACGACGGGATAAGGGATAAAGGGATAAAGCTAGGGATAATAGGGATAAACAGCATGGGATAAGGGGATAAGGGATAATGGGGATAATGGGATAAGGGATAAGGGATAACGGGATAACCTCTAGGGGATAAGGGATAATGGGATAATGGGATAAGAGGGATAAGGGATAACGGGATAAGGGGATAAGGGGGATAAAGGGATAACCGAAAGGGGATAACGGCGGGATAACGCTAGGAAGGGATTTAATGGGATAACGGGGGATAACCAGGGGATAAGGGATAAAGCCGGGATAAGTTTGGGATAAGGGATAAGCGAAGGGATAAGGGGATAAGGGATAATGTCGGGGATAAACGGGATAAGGGATAAATGGGATAATGGGGATAAGGGATAATATAGGGATAAGGGGATAAGAGGGATAATGGGATAAGGGATAACCCGCGGGATAAATGGGATAACATCGGGATAAATGT"
subseq = "GGGATAAGG"
index_list = []
n = len(subseq)
for i in range(len(seq)-n):
	if seq[i:i+n] == subseq:
		index_list.append(str(i+1))
output = " ".join(index_list)
print("%s" %output)
