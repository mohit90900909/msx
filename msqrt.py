x = [100,0,0,20,23]
y = []
y = [t for t in x if t!=0]
n = x.count(0)
for i in range (n):
	y.append(0)
print(y)

