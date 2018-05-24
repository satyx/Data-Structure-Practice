class node:
	def __init__(self,data):
		self.data=data
		self.next=None

def precedence(x):
	if x in ('+','-'):
		return 0
	elif x in ('*','/'):
		return 1
	elif x=='^':
		return 2
	elif x==')':
		return 3


exp,opr=None,None

inp=input("Enter the infix expression:")

symbols=('+','-','*','/','^','(',')')
for i in inp[-1::-1]:
	if i==' ':
		continue
	ch=ord(i)
	if ch>=65 and ch<=90 or ch>=97 and ch<=122:
		nd=node(i)
		nd.next=exp
		exp=nd
		
	elif i in symbols:
		if i=='(':
			while opr!=None:
				if opr.data==')':
					opr=opr.next
					break
				else:
					nd=node(opr.data)
					nd.next=exp
					exp=nd
					opr=opr.next
		else:
			while True:
				if opr==None:
					nd=node(i)
					nd.next=opr
					opr=nd
					break
				elif precedence(opr.data)>=precedence(i) and opr.data!=')':
					nd=node(opr.data)
					nd.next=exp
					exp=nd
					opr=opr.next
				else:
					nd=node(i)
					nd.next=opr
					opr=nd
					break
while opr!=None:
	nd=node(opr.data)
	nd.next=exp
	exp=nd
	opr=opr.next
print("The prefix expression :",end=" ")
while exp!=None:
	print(exp.data,end="")
	exp=exp.next
print()
