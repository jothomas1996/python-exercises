import sys

def check_if_pandigital(string):
	""" Check if value is pandigital with digits repeating exactly once"""
	valueSet = set()
	for i in string:
		if i not in valueSet:
			valueSet.add(i)
		else:
			return(0)

	#Checking if all digits from 1 to 9 are present
	for i in range(1,10):
		if str(i) not in valueSet:
			return(0)
	return(1)

def scan():
	""" Scan upto limits for unusual products """
	print 'Scanning for unusual products'
	calculationCount, unusualCount = 0, 0
	checked = [] #List to hold checked pairs
	unusual = [] #List to hold found unusual products
	for m in range(40):
		for n in range(200):
			#Check if this calculation has occured before
			if set([m,n]) not in checked:
				sys.stdout.write('\r' + 'Calculation ' + str(calculationCount + 1) + ', Unusual Products : ' + str(pandigitalCount))
				sys.stdout.flush()
				string = str(m) + '*' + str(n) + '=' + str(m * n)
				checked.append(set([m,n]))
				calculationCount += 1
				if check_if_pandigital(string):
					unusualCount += 1
					print '\n', string
					unusual.append(string)
	return unusual, calculationCount, unusualCount

def cli():
	""" Main function """
	unusual, calculationCount, unusualCount = scan()

	#Print out values
	print '\n\nValues Found : '
	for i in unusual:
		print i

	print '\nTotal number of calcuulations made : ', calculationCount
	print 'Total number of Pandigitals found : ', unusualCount

if __name__ == '__main__':
	cli()