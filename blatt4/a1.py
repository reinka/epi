import math

global n 

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

#Testing isPrime(x)
#for num in range(0, 100):
#	print str(num) + ' ' + str(isPrime(num)) 



#Function calculating the biggest pandigital number with n digits
def biggest_pan(n):
	biggest = 0
	while(n > 0):
		 biggest += n*10**(n-1)
		 n -= 1

	return biggest

#Testing biggest_num(n)
#print biggest_pan(n) 

#Function calculating the n-th digit of a number
def nth_digit(x, n):
	while(n > 0):
		num = x%10
		x /= 10
		n -= 1
	return num

#Testing nth_digit(x,n)
#for num in range(1, n+1):
#	print nth_digit(biggest_pan(n), num)



#Function calculating the digit sum of a number x
def digit_sum(x):
	temp = x
	dig_sum = 0
	while(x > 0):
		dig_sum += x%10
		x /= 10
		dig_sum
	return dig_sum
#Testing digit_sum(x)
#print digit_sum(12345)

#Function which checks if a digit of x is within range [1-n]
def is_range(x):
	in_range = True
	for i in range(1, n+1):
		if(nth_digit(x, i) in range(1, n+1)):
			pass
		else:
			in_range = False
	return in_range
#Testing is_range(x)
#n = 4
#print is_range(4235)

#Function which checks if a digit is being repeated within a n-digital number
def repeat_digit(x):
	no_repeat = True
	for num in range(1, n+1):
		if str(num) not in str(x):
			no_repeat = False
	return no_repeat
#Testing repeat_digit(x)
#n = 5
#print repeat_digit(12245)


#Main function calculating the largest pandigital prime, given n, which will be 
#asked as input
def largest_pandigital_prime():
	global n
	n = input("Choose n (range 1-9):")
	while(biggest_pan(n) % 3 == 0):
		n -= 1
	
	while(n>1):
		x = biggest_pan(n)
		print "Largest pandigital number:", x
		print "n =", n
		while(x>0):
			if(isPrime(x)):
				if(is_range(x)):
					if(digit_sum(x) == digit_sum(biggest_pan(n))):
						if(repeat_digit(x)):
							print "Largest pandigital prime number:",x
							n =- 1
							break
						else:
							x -= 1
					else:
						x -= 1
				else: 
					x -= 1
			else:
				x -= 1

		if(x==0):
			n -= 1

		if(n==1):
			print "There is no pandigital prime within that range"




largest_pandigital_prime()
		

