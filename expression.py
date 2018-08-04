class tree:
	def __init__(self,data):
		self.data=data
		self.lchild=None
		self.rchild=None


inp=input("Expression:")
exp=[]
opr=[]

symbol=['+','-','*','/','(',')','^']


def rearrange(exp,opr):
	nd=opr.pop()
	nd.rchild=exp.pop()
	nd.lchild=exp.pop()
	exp.append(nd)

def priority(opr):
	return {
		'+':0,
		'-':0,
		'*':1,
		'/':1,
		'^':2
		}[opr]

def display(node):
	if node==None:
		return
	display(node.lchild)
	print(node.data,end='')
	display(node.rchild)

for i in inp:
	if i in symbol:
		if i=='(':
			opr.append(tree(i))
		elif i==')':
			while opr[-1].data!='(':
				rearrange(exp,opr)
				if len(opr)==0:
					break
			opr.pop()

		elif len(opr)==0:
			opr.append(tree(i))
		else:
			if opr[-1].data=='(' or priority(opr[-1].data)<priority(i):
				opr.append(tree(i))
			else:
				while priority(opr[-1].data)>=priority(i):
					rearrange(exp,opr)
					if len(opr)==0 or opr[-1].data=='(':
						break
				opr.append(tree(i))
	else:
		exp.append(tree(i))

while len(opr)>0:
	rearrange(exp,opr)

print('Expression stored in tree:',end='')
if len(exp)!=0:
	display(exp.pop())
else:
	print()
print()
