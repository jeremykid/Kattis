
def main():
	l = raw_input('')
	l = l.split(' ')
	H = int(l[0])+1
	try:
		direction = list(l[1])
		temp = 1
		index = 0
		for i in direction:
			index += 1
			if i == "L":
				temp *= 2
			if i == "R":
				temp *= 2
				temp += 1
		result =2**H - temp
		print result
	except:
		print 2**H-1
main()