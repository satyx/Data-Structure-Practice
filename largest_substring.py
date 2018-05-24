t=int(input())
while t>0:
	count=0
	stack=[]
	maxi=0
	inp=input()
	for i in inp:
		if i==' ':
			continue
		if i=='(':
			stack.append(i)	
		if i==')':
			if len(stack)>0:
				count+=1
				stack.pop()
			elif len(stack)==0:
				if maxi<count:
					maxi=count
				count=0
	if maxi<count:
		maxi=count
	print(2*maxi)
	t-=1
