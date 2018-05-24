test=int(input())
start=('(','{','[')
while test>0:
	a=list()
	flag=True
	exp=input()
	for i in exp:
		if i in start:
			a.append(i)
		elif i==')':
			if len(a)==0:
				flag=False
				break
			if a.pop()!='(':
				flag=False
				break
		elif i=='}':
			if len(a)==0:
				flag=False
				break
			if a.pop()!='{':
				flag=False
				break
		elif i==']':
			if len(a)==0:
				flag=False
				break
			if a.pop()!='[':
				flag=False
				break
	if flag==False:
		print("not balanced")
	elif len(a)!=0:
		print("not balanced")
	else:
		print("balanced")
	test-=1		
