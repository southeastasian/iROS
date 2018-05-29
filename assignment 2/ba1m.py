def numberToPattern(x, k):
	if k == 1:
		return numberToSymbol(x)
	return numberToPattern(x // 4, k-1) + numberToSymbol(x % 4)

def numberToSymbol(x):
	if x == 0:
		return "A"
	if x == 1:
		return "C"
	if x == 2:
		return "G"
	if x == 3:
		return "T"

print(numberToPattern(5353,7))
	
#conversion from number to pattern using number to symbol method (index numbers to AGCT)
#mathematical calculation from decimal system to 4/number-system (simple division/rest calculations)
#opposite to patterntonumber 
