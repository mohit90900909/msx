import sys 
n = len(sys.argv)
args = sys.argv
for i in args:
	try:
		print(int(i,16))
	except:
		continue
