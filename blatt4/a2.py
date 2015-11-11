import math

def digit_count(x):
	#x = input("Enter an integer:")
	temp = x
	count = 0
	while(x):
		count += 1
		x /= 10
	#print "%d consists of %d digits" % (temp, count)
	return count
#Test
#digit_count(1321)


#Function calculating the n-th digit of a number x
def nth_digit(x, n):
	while(n > 0):
		num = x%10
		x /= 10
		n -= 1
	return num

#Function deleting the n-th digit in a number
def del_digit(x, n):
	new = 0
	i = 0
	for num in range(1, digit_count(x)+1):
		if(num != n):
			new += nth_digit(x, num)*10**i
			#print "del_digit:",new
		else:
			continue
		i += 1

	return new
#Testing del_digit(x,n)
#print del_digit(547, 3)

def isPrime(x):
	if(x == 0 or x == 1):
		prime = False
	else:
		prime = True

	if(not(x % 2) and not 2):
			prime = False
			return prime

	for num in range(2, int(math.sqrt(x)+1)):
		if(x % num):
			prime = True
		else:
			prime = False
			return prime

	return prime


count = 0
start = 11

while(count <11):
	prime = True
	temp = start
	#print "temp start:", temp
	digit_num = digit_count(start)
	#print "digit_num:", digit_num

	if(isPrime(start)):
		while(digit_num > 1):
				temp = del_digit(temp, digit_num)
				#print "TEmp:", temp, start
				if(isPrime(temp)):
					digit_num -= 1
				else:
					start += 1
					prime = False
					break
#
		digit_num = digit_count(start)
		i = 1
		temp = start

		while((i < digit_num) and prime):
			temp = del_digit(temp, 1)
	#		print "TEmp2:", temp, start
			if(isPrime(temp)):
				i += 1
			else:
				i += 1
	#			print "No Prime", temp
				break

		if(isPrime(temp)):
			print "Truncatable prime found:", start
			count += 1
			start += 1
		else:
			start += 1	
	else:
		start += 1