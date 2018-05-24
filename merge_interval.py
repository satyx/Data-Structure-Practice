test=int(input())
while test>0:

	n=int(input())
	inp=[int(i) for i in input().split()]
	i=0
	col=[]
	while i<n:
		col.append([inp[2*i],inp[2*i+1]])
		i+=1
	i=0
	while i<n-1:
		j=0
		while j<n-i-1:
			if col[j][0]==col[j+1][0]:
				if col[j][1]<col[j+1][1]:
					col[j],col[j+1]=col[j+1],col[j]
			if col[j][0]>col[j+1][0]:
				col[j],col[j+1]=col[j+1],col[j]
			j+=1
		i+=1

	i=0
	while i<n-1:
		if col[i][1]>=col[i+1][0]:
			if col[i][1]<col[i+1][1]:
				col[i][1]=col[i+1][1]
			del col[i+1]
			n-=1
		else:
			i+=1
	i=0

	for i in col:
		print(*i,end=" ")
	print()
	test-=1
