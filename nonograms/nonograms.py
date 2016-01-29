
def read(line):
	l =[]
	count =0; 
	print (line)
	prevChar = " "
	for i,x in enumerate(line):
		#print("current char is "+x+"  prev char is "+prevChar)
		if i == 1 and x =="*":
			count = 1 
		if prevChar == " " and x=="*":
			count = 1
		elif prevChar =="*" and x=="*":
			count+=1
		elif prevChar =="*" and x==" ":
			#print("found space")
			l.append(count)
			count =0
		elif prevChar =="*" and (x=="\n") :
			l.append(count)
		if x=="\n":
			break
		prevChar =x
	return l; 

def main():
	f = open("input.txt","r")
	noLines = sum(1 for l in f)
	flist= []
	print("Number of lines ",noLines)
	f.seek(0)
	for i in range(0,noLines):
		flist.append(f.readline())
	#print(flist)
	for i in flist:
		l = read(i)
		print(l)
	#l = read(flist[2])
	#print(l)


if __name__ == "__main__":
    main()