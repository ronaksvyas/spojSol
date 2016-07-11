
def main():
	t = long(raw_input())
	# getPrimeFactors(t)
	# exit(1)
	i = long(0)
	for i in xrange(t):
		n = long(raw_input())
		findNumZeroes(n)
def findNumZeroes(n):
	countOf5 = 0
	countOf2 = 0
	for k in xrange(2,n+1):
		primeFactors = getPrimeFactors(k)
		# print primeFactors
		for i in xrange(len(primeFactors)):
			if(primeFactors[i] == 5):
				countOf5+=1
			if(primeFactors[i] == 2):
				countOf2+=1
	print min([countOf2,countOf5])

def getPrimeFactors(n):
	factors = []
	limit = long(100000000)
	i = 2
	while(n > 1 and i <= n and i < limit):
		if(n%i == 0):
			factors.append(i)
			n = n / i
		else:
			i+=1
	# print factors
	return factors
if __name__ == '__main__':
	main()
