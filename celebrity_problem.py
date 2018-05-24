t=int(input("Test Cases:"))
while t>0:
	n=int(input("Number of people:"))
	arr=[int(i) for i in input("Enter the matrix:").split()]

	inter=[i for i in range(1,n)]
	cel=[]
	x=0
	while len(inter)>0:
		while len(inter)>0:
			a=inter.pop()
			if arr[n*x+a]==1:
				cel.append(a)
		if len(cel)==0:
			break
		else:
			x=cel.pop()
			inter=cel
			cel=[]
	test=-1
	check=False
	if x==n-1:
		test=n-2
	else:
		test=n-1

	for i in range(n):
		if arr[n*x+i]!=0:
			x=-1
			break
		if test>=0:
			if arr[n*test+i]==1:
				check=True
				
				
	if check==True:
		print("Celebrity Index :",x)
	else:
		print("Celebrity Index :",-1)
	t-=1

