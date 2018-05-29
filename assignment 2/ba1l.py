def patternToNumber(pattern):
	if len(pattern) == 0:
		return 0
	return 4 * patternToNumber(pattern[0:-1]) + symbolToNumber(pattern[-1:])

def symbolToNumber(symbol):
	if symbol == "A":
		return 0
	if symbol == "C":
		return 1
	if symbol == "G":
		return 2
	if symbol == "T":
		return 3

print(patternToNumber("CTTCTCACGTACAACAAAATC"))

#conversion from pattern to number using symbol-to-number method (A/G/C/T to index numbers)
#mathematical calculations from 4-number-system to decimal system 
