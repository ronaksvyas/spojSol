import math

def main():
	n = int(raw_input())
	allPrimes = primes_sieve2(1000000000)
	primes = {}
	for k in allPrimes:
		primes[k] = True
	for i in xrange(0,n):
		x = map(long, raw_input().split())
		for j in xrange(x[0] , x[1]+1):
			if(primes.has_key(j)):
				print(j)

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

if __name__ == '__main__':
	main()
