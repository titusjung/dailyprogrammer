
def read(line):
	l =[]
	count =0; 
	prevChar=" "
	#print (line)
	for i,x in enumerate(line):
		#print("current char is "+x+"  prev char is "+prevChar)
		#print("x is "+x)
		#print(i)
		if i == 0 and x =="*":
			count = 1 
		if prevChar == " " and x=="*":
			count = 1
		elif prevChar =="*" and x=="*":
			count+=1
		elif prevChar =="*" and x==" ":
			#print("found space")
			l.append(count)
			count =0
		elif prevChar =="*" and "\n" in x :
			#print("new line reached")
			l.append(count)
		if i is len(line)-1 and x is"*":
			l.append(count)
			#print("new line reached")
			break
		prevChar =x
	#print("count is ",count) 
	return l; 

def main():
	f = open("input2.txt","r")
	noLines = sum(1 for l in f)
	flist= []
	print("Number of lines ",noLines)
	matrix = []
	tempList = []
	f.seek(0)
	for i,l in enumerate(range(0,noLines)):
		l = f.readline()
		tempList = []
		for j in l:
			if j is not "\n":
				tempList.append(j)
		matrix.append(tempList)
	#print(matrix)
	height = len(matrix)
	hList =[]
	vList = []
	for i in matrix:
		#print(i)
		hList.append(read(i))
	print(hList)
	for j in range(height):
		tempVList =[]
		for i in range(len(matrix)):
			tempVList.append(matrix[i][j])
		#print(tempVList)
		vList.append(read(tempVList))
	print(vList)
	#l = read(flist[4])
	#print(l)


if __name__ == "__main__":
    main()