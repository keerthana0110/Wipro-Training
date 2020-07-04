maximum = int(input())
minimum = int(input())

print("".format(maximum, minimum)) 

while ( maximum >= minimum):
    print (maximum, end = '  ')
    maximum = maximum - 1
