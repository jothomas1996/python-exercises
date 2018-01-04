'''
Pandigital is a number in which if there are n digits then the number
will contain all digits from 1 to n at least once. An example for a 7
pandigital number is 2135467.
'''

def check_if_pandigital(string):
	""" Check if value is pandigital with digits repeating exactly once"""
	valueSet = set()
	for i in string:
		if i not in valueSet:
			valueSet.add(i)
		else:
			return(0)

	#Checking if all digits are present
	for i in range(10):
		if str(i) not in valueSet:
			return(0)

	return(1)

def cli():
	""" Main function """
	print 'Scanning for pandigital values'
	calculationCount, pandigitalCount = 0, 0
	for m in range(1000):
		for n in range(10000):
			string = str(m) + '*' + str(n) + '=' + str(m * n)
			calculationCount += 1
			if check_if_pandigital(string):
				pandigitalCount += 1
				print string
	print '\nTotal number of calcuulations made : ', calculationCount
	print 'Total number of Pandigitals found : ', pandigitalCount

if __name__ == '__main__':
	cli()