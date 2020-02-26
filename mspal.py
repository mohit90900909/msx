x = input("enter the string")
x = x.lower()
t = ord('a')
for i in range(ord("a"),ord("z")+1):
	n = x.count(chr(i))
	if n==0:
		print("not pangram")
		break

if i == ord("z"):
	print("pangram")

