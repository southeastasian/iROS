import math

pattern = "AAA"
DNAs = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]

def HammDistance(str1, str2):
    Hdist = 0
    for k,i in zip(str1, str2):
        if k != i:
            Hdist += 1
    return Hdist

# Function to calculate the Hamming Distance with Input = 2 Strands with varied Lengths and Output = Integers
# Initiating the count variables and add 1 if the input doesn't match 

# Function to calculate the distance between pattern and DNA Sequences; Input= pattern, dna sequences with integers as Output
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

# Setting Hammingdistance to infinity (maximum)
# Using intermediate variables to exclude double counts 
# Hammingdistance is the smallest integer registered 
# Summing up the smallest output (Hammingdistance) every dna sequences, which have undergone the function-loop

print(DistanceBetweenPatternAndStrings(pattern, DNAs))
