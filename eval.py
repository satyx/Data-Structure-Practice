opr=[]
num=[]

def evaluate(x,y,opr):
	if opr=='+':
		return x+y
	elif opr=='-':
		return x-y
	elif opr=='*':
		return x*y
	elif opr=='/':
		return x/y
	elif opr=='^':
		return x**y

def precedence(opr):
	if opr in ('+','-'):
		return 0
	elif opr in ('*','/'):
		return 1
	elif opr=='^':
		return 2
	elif opr=='(':
		return 3
symbols=('+','-','*','/','^','(',')')
for i in input("Enter the expression:"):
	if i>='0' and i<='9':
		num.append(int(i))
		continue
	elif i in symbols:
		if i==')':
			while opr!=None:
				operation = opr.pop()
				if operation=='(':
					break
				x=num.pop()
				y=num.pop()
				result=evaluate(y,x,operation)	#note the order of arguments
				num.append(result)
				
		else:
			while True:
				if len(opr)==0:
					opr.append(i)
					break
			
				elif precedence(i)>=precedence(opr[len(opr)-1]) or opr[len(opr)-1]=='(':	#opr[len(opr)-]=opr.pop()
					opr.append(i)
					break
				else:
					operation=opr.pop()
					x=num.pop()
					y=num.pop()
					result=evaluate(y,x,operation)
					num.append(result)

while len(opr)>0:			#There is no chance that there is ( or ). Only there are mathematical binary operations
	i=opr.pop()
	x=num.pop()
	y=num.pop()
	result=evaluate(y,x,i)
	num.append(result)

if num[0]==int(num[0]):
	print(int(num[0]))
else:
	print(num[0])
