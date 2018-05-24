t=int(input())
while t>0:
	n=int(input())
	t-=1
	num=[int(i) for i in input().split()]
	i=1
	stackL=[]
	stackR=[]
	x=[[] for i in num]
	stackL.append([num[-1],n-1])
	stackR.append([num[0],0])
	while i<n:
		if num[i]<stackR[-1][0]:
			while len(stackR)>0:
				if num[i]<stackR[-1][0]:
					x[stackR[-1][1]].insert(1,num[i])
					stackR.pop()
					
				else:
					break

			stackR.append([num[i],i])
		else:
			stackR.append([num[i],i])

		if num[n-1-i]<stackL[-1][0]:
			while len(stackL)>0:
				if num[n-1-i]<stackL[-1][0]:
					x[stackL[-1][1]].insert(0,num[n-1-i])
					stackL.pop()
				else:
					break

			stackL.append([num[n-1-i],n-1-i])
		else:
			stackL.append([num[n-1-i],n-1-i])
		i+=1
	while len(stackR)>0:
		temp=stackR.pop()
		x[temp[1]].insert(1,0)
	while len(stackL)>0:
		x[stackL.pop()[1]].insert(0,0)
	maxi=0
	for i in x:
		if abs(i[1]-i[0])>maxi:
			maxi=abs(i[1]-i[0])
	print(maxi)
