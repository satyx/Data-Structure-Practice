t=int(input())
while t>0:
	t-=1
	num=[int(i) for i in input().split()]
	greater=[-1 for i in num]
	smaller=[-1 for i in num]
	
	n=len(num)
	i=n-1
	stack=[]
	while i>=0:
		while len(stack)>0 and num[i]<=num[stack[-1]]:
			stack.pop()

		if len(stack)>0:
			greater[i]=stack[-1]
		stack.append(i)
		i-=1
	print(greater)
	stack=[]
	count=0
	for i in greater[-1::-1]:
		if i==-1:
			print("hi")
			count+=1
			continue
		print("hola")
		while len(stack)>0 and num[i]<=stack[-1]:
			stack.pop()
			print("mew")
		if len(stack)>0:
			smaller[count]=num[stack[-1]]
		stack.append(num[i])
		count+=1
		print("bow")
	print(smaller)
