def main():
	t = int(raw_input())
	for i in xrange(t):
		n = long(raw_input())
		getNextPalindrome(n)


def getNextPalindrome(n):
	ns = list(str(n))
	if(isPalindrome("".join(ns))):
		print "".join(ns)
		return
	if(len(ns) == 1):
		print 11
		return
	else:
		i = 0
		j = len(ns) - 1
		for i in xrange(len(ns)/2):
			ns[len(ns)-i-1] = ns[i]
		while(isPalindrome("".join(ns)) == False):
			ns = list(str(long("".join(ns))+1))
		print "".join(ns)



def isPalindrome(n):
	n = str(n)
	if(n[::-1] == n):
		return True
	else:
		return False

if __name__ == '__main__':
	main()