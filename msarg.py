import argparse
parser = argparse.ArgumentParser(description="this program does the square of a number")
parser.add_argument("Num",type = int,help = "please input the integer type number")
args = parser.parse_args()
result = args.Num**2
print(result)

