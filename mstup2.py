x = input("enter your data")
x.split()
t = []
for i in x:
	if i.isalpha():
		t.append(i)
	else:
		t.append(eval(i))
print(t)
