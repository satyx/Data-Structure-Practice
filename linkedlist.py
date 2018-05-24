class node:
	def __init__(self,data):
		self.data=data
		self.next=None

class linkedlist:
	def __init__(self):	
		self.head=None

def main():
	llist=linkedlist()
	count=0
	print("1.Add\n2.Delete\n3.Search\n4.Print\n5.Swap Nodes\n6.Middle Element(s)\n7.Reverse List\n8. Duplicate removal(if list is sorted\n9.Pairwise Swap elements\n0.Quit")
	while True:
		
		ch=int(input("Enter your choice:"))
		if ch==0:
			print("quitting.....")
			break
		elif ch==1:
			if llist.head!=None:
				nd=node(input("Enter the data:"))
				llist.head,nd.next = nd,llist.head
				count+=1
			else:
				llist.head=node(input("Enter data:"))
				count=1
		elif ch==2:
			if llist.head==None:
				print("Empty")	
				continue
			temp=llist.head
			llist.head=llist.head.next
			del temp
			count-=1
			print("Deleted Successfully")
		elif ch==3:
			Result=False
			if llist.head==None:
				print("Empty List")
				continue
			sr=input("Enter the data to be searched:")
			temp=llist.head
			while temp!=None:
				if temp.data==sr:
					Result=True
					break
				else:
					temp=temp.next
			if Result == False:
				print("Search Unsuccessful")
			else:
				print("Search Successful")

		elif ch==4:
			if llist.head==None:
				print("Empty")
				continue
			temp=llist.head
			while temp!=None:
				print(str(temp.data), end="->")
				temp=temp.next
			print("End")
			print("total ",count)
	
		elif ch==5:
			a,b=(int(i) for i in input("Enter the nodes followed by space:").split())
			if a>count or b>count or a*b<=0:
				print("Wrong data entered.\nAborting................")
				quit()

			if a==b:
				print("Swapped Successfully")
				continue
			if a<0:
				a+=count+1
				b+=count+1
				if a<=0 or b<=0:
					print("Wrong data Entered.\nAborting..........")
			temp=llist.head		
			num=1				#loop variable
			prev_a,prev_b,curr_a,curr_b=None,None,None,None		#Stores the reference of the node
			while num<a or num<b:
				if num<a:
					prev_a=temp
				if num<b:
					prev_b=temp
				num+=1
				temp=temp.next
			if prev_a==None:
				curr_a=llist.head
				curr_b=prev_b.next
				llist.head=curr_b
				prev_b.next=curr_a

				curr_a.next,curr_b.next=curr_b.next,curr_a.next
			elif prev_b==None:
				curr_b=llist.head
				curr_a=prev_a.next
				llist.head=curr_a
				prev_a.next=curr_b

				curr_a.next,curr_b.next=curr_b.next,curr_a.next
			else:
				curr_a=prev_a.next
				curr_b=prev_b.next
				prev_a.next,prev_b.next=curr_b,curr_a
				curr_a.next,curr_b.next=curr_b.next,curr_a.next
			print("Swapped Successfully")
		
		elif ch==6:
			if count==0:
				print("Empty List")
				continue
			mov_1=mov_2=llist.head
			while True:
				if mov_2.next==None:
					print("Middle element is",mov_1.data)
					break
				elif mov_2.next.next==None:
					print("Middle elements are",mov_1.data,"and",mov_1.next.data)
					break
				else:
					mov_1=mov_1.next
					mov_2=mov_2.next.next

		elif ch==7:
			if count==0:
				print("Empty List")
				continue
			curr=llist.head
			top=None
			while curr!=None:
				nd = node(curr.data)
				nd.next=top
				top=nd
				temp=curr
				curr=curr.next
				del temp
			llist.head=top
			print("Successfully Reversed")
			
		elif ch==8:
			if count==0:
				print("Empty List")
				continue
			temp=llist.head
			while temp.next!=None:
				if temp.data==temp.next.data:
					removal=temp.next
					temp.next=temp.next.next
					del removal
					count-=1
					continue
				else:
					temp=temp.next
			print("Duplication removal successful")

		elif ch==9:
			if count==0:
				print("Empty List")
				continue
			elif count==1:
				print("Successfully pairwise swapped")
				continue
			curr_x=llist.head
			curr_y=curr_x.next
			prev=None
			llist.head=curr_y
			curr_x.next,curr_y.next=curr_y.next,curr_x

			try:
				while curr_x.next.next!=None:
					prev=curr_x
					curr_x=curr_x.next
					curr_y=curr_x.next
		
					prev.next=curr_y
					curr_x.next,curr_y.next=curr_y.next,curr_x
			except:
				pass	#Null statement
				'''
				sat
				'''
			finally:
				print("Succuessfuilly pairwise swapped")

		else:
			print("Wrong Data Entered.\nAborting.........")
			quit()

main()
