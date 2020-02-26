x = input("enter the numers").split()
n = []
for i in x:
	p = 1
	for t in range(1,int(i)+1):
		p *= t
	n.append(p)
print(n)

			
	
