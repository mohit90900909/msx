x = (1,2,6,5,4,1, 2, 3, 4, 5, 6,7)
x = list(x)
t = []
y = []
for i in x:
	if i not in t:
		t.append(i)
	else:
		y.append(i)
y = tuple(y)
print(y)
	

