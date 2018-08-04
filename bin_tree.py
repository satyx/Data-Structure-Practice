q=[0 for i in range(32)]
def node_creation_by_choice(data,parent,child):
	global q
	if q[parent-1]==0:
		new_node(data)
		return
	q[2*parent+child-1]=data
	
def new_node(data):
	temp=[]
	global q
	temp.append(1)
	key=1
	while len(temp)!=0:
		if q[2*temp[0]-1]==0:
			q[2*temp[0]-1]=data
			break
		elif q[2*temp[0]]==0:
			q[2*temp[0]]=data
			break
		else:
			del(temp[0])
			if 2*key+1<32:
				temp.append(2*key)
				temp.append(2*key+1)

q[0]=int(input("Root:"))
while(True):
	ch=int(input('Choice:'))
	if ch==0:
		break
	else:
		node_creation_by_choice(int(input('Data:')),int(input('Parent:')),int(input('Child:')))
print(q)
