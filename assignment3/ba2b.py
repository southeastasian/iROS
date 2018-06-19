import math

def NumberToPattern (index, k):
    if k == 1:
        return NumberToSymbol(index)
    return NumberToPattern(index // 4, k-1) + NumberToSymbol(index % 4)

# 4^k combinations of kmers 

def NumberToSymbol(zahl):
    if zahl == 0:
        return "A"
    if zahl == 1:
        return "C"
    if zahl == 2:
        return "G"
    if zahl == 3:
        return "T"

# converting the four base pairs to defined numbers 

def HammDistance(str1, str2):
    Hdist = 0
    for k,i in zip(str1, str2):
        if k != i:
            Hdist += 1
    return Hdist

def DistanceBetweenPatternAndStrings(pattern, dna):
	k = len(pattern)
	distance = 0
	for t in dna:
		HammingDistance = math.inf
		for kmer in range(len(t) - k + 1):
			ZwHDist = HammDistance(pattern, t[kmer:kmer+k])
			if ZwHDist < HammingDistance:
				HammingDistance = ZwHDist
		distance += HammingDistance
	return distance

def MedianString(DNA, k):
	distance = math.inf
	for i in range (4**k-1):
		currentpatt = NumberToPattern(i, k)
		ZwHDist = DistanceBetweenPatternAndStrings(currentpatt, DNA)
		if ZwHDist < distance:
			distance = ZwHDist
			Median = currentpatt
	return Median

length = 3
DNAs = ["AAATTGACGCAT", "GACGACCACGTT", "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTACGGGACAG"]
lp = 6
seq = ["TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT", "CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA", "TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT", "TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA", "ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG", "TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA", "TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC", "GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA", "CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG", "CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG"]

# Finding out which kmers with the list of dna sequences show the smallest Hammingdistance-Output; using MedianString Function

print(MedianString(seq, lp))
