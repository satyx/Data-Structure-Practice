t=int(input())
while t>0:
	t-=1
	inp=input()
	out=''
	i=0
	opp={'+':'-','-':'+'}
	history=[]
	while i<len(inp):
		if inp[i]=='+' or inp[i]=='-':
			if len(history)==0 or history[-1]=='+':
				out+=inp[i]
				if inp[i+1]=='(':
					history.append(inp[i])
			else:
				out+=opp[inp[i]]
				if inp[i+1]=='(':
					history.append(opp[inp[i]])

		elif inp[i]==')':
			history.pop()
		elif inp[i]!='(':
			out+=inp[i]
		i+=1
	print(out)
