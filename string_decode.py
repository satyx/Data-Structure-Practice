t=int(input())
while t>0:
	t-=1
	inp=input()
	code=[]
	for i in inp:
		temp=''
		num=0
		fre=[]
		if i==']':
			while True:
				ch=code.pop()
				if ch=='[':
					try:
						while True:					
							fre.append(int(code[-1]))
							code.pop()
					except:
						pass
					break
				else:
					temp+=ch
			while len(fre)>0:
				num=num*10+fre.pop()
			temp*=num
			for j in temp[-1::-1]:
				code.append(j)

		else:
			code.append(i)
	final=[]
	while len(code)>0:
		final.append(code.pop())
	while len(final)>0:
		print(final.pop(),end="")
	print()
