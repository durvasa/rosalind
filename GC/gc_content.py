#!/usr/bin/python3

def FASTA_iterator(fasta_filename):
	
	"""
	A Generator Function that reads a FASTA file. In each iteration, the
	function must return a tuple with the format (identifier, sequence)
	"""
	
	fasta = open(fasta_filename,"r")
	sequence = ""
	identifier = ""
	my_list = []
	for line in fasta:
		if (line[0] == ">"):
			if (sequence != ""):
				my_tuple = (identifier, sequence)
				yield(my_tuple)
				identifier= ""
				sequence= ""
			identifier = line[1:].strip()
		else:
			sequence += line.strip()
	my_tuple=(identifier, sequence)
	yield(my_tuple)
	fasta.close

if __name__ == '__main__':

	"""	Computes the GC-content and returns the entry with max GC-content"""
	
	max_gc_cont = 0
	for entry in FASTA_iterator("file.fa"):
		gc_cont = 0
		counter = 0
		for char in entry[1]:
			counter += 1
			if char == "C" or char == "G":
				gc_cont += 1
		gc_cont *= 100/counter
		if gc_cont > max_gc_cont:
			max_gc_cont = gc_cont
			identifier = entry[0]
	print("%s\n%.6f" %(identifier,max_gc_cont))
			
			
