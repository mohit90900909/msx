z = {}
n = int(input("enter the number of players"))
for i in range(n):
	x = input("enter the name of the player: ")
	y = int(input("enter the score of the player: "))
	z.update({x:y})
x  = input("enter the name of the player")
n = z.get(x,-1)
if n==-1:
	print("name not found")
else:
	print("{0} scored {1}".format(x,n))