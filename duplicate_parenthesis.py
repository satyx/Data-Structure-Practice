t=int(input())
while t>0:
	t-=1
	inp=input()
	stack=[]
	dup=False
	for i in inp:
		if i==')':
			if stack[-1]=='(':
				dup=True
				break
			while len(stack)>0:
				if stack[-1]=='(':
					stack.pop()
					break
				stack.pop()
		else:
			stack.append(i)
	if dup==True:
		print("Duplicate")
	else:
		print("Not Duplicate")
