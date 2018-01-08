import sys

def check_if_pandigital(string):
	""" Check if value is pandigital with digits repeating exactly once"""
	valueSet = set()
	for i in string:
		if i not in valueSet:
			valueSet.add(i)
		else:
			return(0)
	#Check if 0 is present
	if '0' in valueSet:
		return(0)
	#Checking if all digits from 1 to 9 are present
	for i in range(1,10):
		if str(i) not in valueSet:
			return(0)
	return(1)

def check_if_required(m,n):
	""" To check if the next calculation is required """
	if m < 10 and n > 999: #1 * 1000 = 1000
		return(1)
	elif m < 100 and n > 99: #10 * 100 = 1000
		return(1)
	elif m >999 and n < 10: #1000 * 1 = 1000
		return(1)
	elif m > 99 and n < 100: #100 * 10 = 1000
		return(1)
	elif len(str(m) + str(n)) == 6: #Discard calculation if length not 6
		return(1)

	return(0)

def scan():
	""" Scan upto limits for unusual products """
	print 'Scanning for unusual products'
	calculationCount, unusualCount = 0, 0
	checked = [] #List to hold checked pairs
	unusual = [] #List to hold found unusual products with operands
	unusualProduct = [] #List to hold found unusual products
	for m in range(9876):
		for n in range(9876):
			#Check if this calculation has occured before
			if set([m,n]) not in checked:
				if check_if_required(m,n): #Check if calculation is required
					sys.stdout.write('\r' + 'Calculation ' + str(calculationCount + 1) + ', Unusual Products : ' + str(unusualCount))
					sys.stdout.flush()
					product = m * n
					string = str(m) + '*' + str(n) + '=' + str(product)
					checked.append(set([m,n]))
					calculationCount += 1
					if check_if_pandigital(string):
						unusualCount += 1
						print '\n', m, '*', n, '=', product
						unusual.append(str(m) + ' * ' + str(n) + ' = ' + str(product))
						unusualProduct.append(product) #Storing the product to list
	return unusualProduct, unusual, calculationCount, unusualCount

def cli():
	""" Main function """
	unusualProduct, unusual, calculationCount, unusualCount = scan()

	#Print out values
	print '\n\nValues Found : '
	for i in unusual:
		print i

	print '\nTotal number of calcuulations made : ', calculationCount
	print 'Total number of unusual products found : ', unusualCount
	print 'Sum of unusual products found : ', sum(unusualProduct)

if __name__ == '__main__':
	cli()