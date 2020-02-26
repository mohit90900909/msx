y = [int(x) for x in input().split(",")]
n = len(y)
x = []
for i in range(1,y[n-1]):
	if i not in y:
		x.append(i)
print(x)
	
