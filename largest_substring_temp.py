test=int(input("test case:"))
while test>0:
	stack=[]
	inp=input()
	result=0
	i=0
	stack.append(-1)
	while i<len(inp):
		if inp[i]=='(':
			stack.append(i)
			
		elif inp[i]==')':
			stack.pop()
			if len(stack)!=0:
				result=max(result,i-stack[-1])
			else:
				stack.append(i)
		i+=1
	print(result)
	test-=1 
