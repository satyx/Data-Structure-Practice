class node:
	def __init__(self,data):
		self.data=data
		self.next=None

f=node(1)
s=node(2)
t=node(3)
fo=node(4)
sl=node(5)
l=node(6)
F=node(7)
S=node(8)
T=node(9)
f.next=s
s.next=t
t.next=fo
fo.next=sl
sl.next=l
F.next=S
S.next=T
T.next=sl

temp=f

count_a=count_b=0
a=b=None
while temp!=None:
	count_a+=1
	temp=temp.next
temp=F
while temp!=None:
	count_b+=1
	temp=temp.next
if count_a>=count_b:
	diff=count_a-count_b
	a,b=f,F
	while diff>0:
		a=a.next
		diff-=1
else:
	diff=count_b-count_a
	a,b=f,F
	while diff>0:
		b=b.next
		diff-=1

while True:
	if a==b:
		print("Point of intersection:",a.data)
		break
	a,b=a.next,b.next

