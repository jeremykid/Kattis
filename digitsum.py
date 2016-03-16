def digitSum(n):
	l_s = list(str(n))
	result = 0
	for i in l_s:
		result += int(i)
	return result

def main():
	number = int(input(''))
	for i in range(number):
		l = raw_input('').split(' ')
		start = int(l[0])
		end = int(l[1])
		result = 0
		for j in range(start,end+1):
			result += digitSum(j)
		print (result)
main()
