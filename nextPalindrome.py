def main():
	t = int(raw_input())
	for i in xrange(t):
		n = long(raw_input())
		getNextPalindrome(n)





def getNextPalindrome(n):
	ns = str(n+1)
	ns = list(ns)
	if(isPalindrome("".join(ns))):
		print "".join(ns)
		return
	if(len(ns) == 1):
		print int(ns)+1
		return
	else:
		i = 0
		j = len(ns) - 1
		while(not(i == j)):
			if(int(ns[i]) == int(ns[j])):
				i += 1
				j -= 1
			else:
				if(int(ns[j]) < int(ns[i])):
					ns[j] = str(int(ns[j]) + 1)
					ns[i] = ns[j]
				else:
					ns[j] = ns[i]
				if(isPalindrome("".join(ns))):
					print "".join(ns)
					return


def isPalindrome(n):
	n = str(n)
	if(n[::-1] == n):
		return True
	else:
		return False

if __name__ == '__main__':
	main()