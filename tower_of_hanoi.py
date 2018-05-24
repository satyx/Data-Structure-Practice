t=int(input("Enter the numbver of test cases:"))
while t>0:
	n=int(input("Enter the number of discs:"))
	ini=[i for i in range(n,0,-1)]
	aux=[]
	fin=[]
	count=0
	while True:
		if len(aux)==0 and len(ini)==0:
			break
		elif len(aux)==0:
			aux.append(ini.pop())
			count+=1
		elif len(ini)==0:
			ini.append(aux.pop())
			count+=1
		elif aux[len(aux)-1]>ini[len(ini)-1]:
			aux.append(ini.pop())
			count+=1
		else:
			ini.append(aux.pop())
			count+=1

		if len(ini)==0 and len(fin)==0:
			break
		elif len(fin)==0:
			fin.append(ini.pop())
			count+=1
		elif len(ini)==0:
			ini.append(fin.pop())
			count+=1

		elif fin[len(fin)-1]>ini[len(ini)-1]:
			fin.append(ini.pop())
			count+=1
		else:
			ini.append(fin.pop())
			count+=1

		if len(aux)==0 and len(fin)==0:
			break
		elif len(fin)==0:
			fin.append(aux.pop())
			count+=1
		elif len(aux)==0:
			aux.append(ini.pop())
			count+=1

		elif fin[len(fin)-1]>aux[len(aux)-1]:
			fin.append(aux.pop())
			count+=1
		else:
			aux.append(fin.pop())
			count+=1

		if len(ini)==0 and len(aux)==0 and len(fin)!=0:
			break
	if n%2!=0:
		temp=fin
		fin=aux
		aux=[i for i in temp]
		del temp

	print(count)
	t-=1
