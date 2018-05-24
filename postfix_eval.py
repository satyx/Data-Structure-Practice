num=[]
opr=[]

input=input("Enter the postfix expression(eg 8 4 2 - /) :").split(" ")
operations=('+','-','*','/','^')
for i in input:
	if i in operations:
		x=num.pop()
		y=num.pop()
		if i=='^':
			num.append(eval(str(y)+'**'+str(x)))
		else:
			num.append(eval(str(y)+i+str(x)))
	else:
		num.append(i)
if num[0]==int(num[0]):
	print(int(num[0]))
else:
	print(num[0])
