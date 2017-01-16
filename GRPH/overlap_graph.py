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

	"""	Computes the 3-overlap directed graph of a list of sequences"""
	
	edge_set = set()
	for tail in FASTA_iterator("file.fa"):
		for head in FASTA_iterator("file.fa"):
			if tail[1] != head[1] and tail[1][-3:] == head[1][:3]:
				edge_set.add((tail[0],head[0]))
	for edge in edge_set:
		print("%s %s" %edge)
