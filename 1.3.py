def minmax(data):
	minnum = data[0]	
	maxnum = data[0]
	for i in range(len(data)):
		if data[i] > maxnum:
			maxnum = data[i]
			
		elif data[i] < minnum:
			minnum = data[i]

	return (minnum, maxnum)		


list00 = [8, 43, 24, 667, 32, 2, 78]
print(minmax(list00))
