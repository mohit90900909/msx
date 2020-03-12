x = eval(input("enter the number of prime numbers you want: "))
def send(number):
    c = 0
    for i in range(2,number):
        if number%i==0:
            break
        else:
            c+=1
    if c == number - 2:
        return number

z = [2]
for i in range(3,1000):
    t = send(i)
    if t is not None:
        z.append(send(i))
for i in range(x):
    print(z[i])