x = input("enter the values")
x = x.split()
t = ""
for i in x:
	if i not in t:
		t = t + i + " "


t = t.split()
print(*t,sep='*')
