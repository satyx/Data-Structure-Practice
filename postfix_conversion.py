class node:
	def __init__(self,data):
		self.data=data
		self.next=None

exp,opr=None,None

def precedence(x):
	if x in ('+','-'):
		return 0
	elif x in ('*','/'):
		return 1
	elif x =='^':
		return 2
	elif x=='(':
		return 3

symbols = ('+','-','*','/','^','(',')')
for i in input():
	if i==' ':
		continue
	ch=ord(i)
	if ch>=65 and ch<=90 or ch>=97 and ch<=122:
		nd=node(i)
		nd.next=exp
		exp=nd
	elif i in symbols:
		if i==')':
			while True:
				if opr==None:
					break
				elif opr.data=='(':
					opr=opr.next
					break
				else:
					nd=node(opr.data)
					nd.next=exp
					exp=nd
					opr=opr.next
		else:
			if opr==None:
				nd=node(i)
				nd.next=opr
				opr=nd
			else:
				if precedence(i)>precedence(opr.data):
					nd=node(i)
					nd.next=opr
					opr=nd
				else:
					
					while opr!=None:
						if opr.data=='(':
							opr=opr.next
							break
						if precedence(opr.data)>=precedence(i):
							nd=node(opr.data)
							nd.next=exp
							exp=nd
							opr=opr.next
						else:
							break
					nd=node(i)
					nd.next=opr
					opr=nd
while opr!=None:
	nd=node(opr.data)
	nd.next=exp
	exp=nd
	opr=opr.next
result=None
while exp!=None:
	nd=node(exp.data)
	nd.next=result
	result=nd
	exp=exp.next
print("Postfix expression:",end=" ")
while result!=None:
	print(result.data,end="")
	result=result.next
print()
