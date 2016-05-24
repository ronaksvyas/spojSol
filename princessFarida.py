def main():
	n = long(raw_input())
	for i in xrange(n):
		numMon = long(raw_input())
		if(numMon == 0):
			raw_input()
			print "Case "+str(i+1)+': '+str(0)
		else:
			coins = map(long,raw_input().split(' '))
			calculateMaxCoins(numMon,coins, i+1)



def calculateMaxCoins(n , coins , case):
	if(n == 1):
		print "Case "+str(case)+': '+str(coins[0])
		return
	csum = [long(0)] * n
	csum[0] = coins[0]
	csum[1] = max(coins[0],coins[1])
	for i in xrange(2,n):
		csum[i] = max(csum[i-1],coins[i]+csum[i-2])
	print "Case "+str(case)+': '+str(csum[n-1])

if __name__ == '__main__':
	main()