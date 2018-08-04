tree=[0 for i in range(32)]

def new_node(data):
	global tree
	tree.append(data)

def delete_node(location):
	global tree
	stack=[1]
	while len(stack)!=0:
		if 2*stack[-1]+1<=len(tree):
			tree(location-1)=tree(2*stack[-1])	
	

while(True):
	ch=int(input("Choice:"))
	if ch==0:
		break
	if ch==1:
		print(tree)
		continue
	if ch==2:
		if len(tree)==0:
			print("Empty")
			continue
		delete_node(int(input("location:")))
		continue
	if tree[0]==0:
		tree[0]=int(input("Root:"))
		continue
	else:
		new_node(int(input("Data:")))
