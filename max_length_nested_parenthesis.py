#Use of stack
inp=input()
par=[]
count=0
maxi=0
for i in inp:
	if i=='(':
		par.append(i)
		count+=1
		if count>maxi:
			maxi=count
	elif i==')':
		par.pop()
		count-=1
	else:
		continue

print(maxi)
