n=int(input("enter any number: "))
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()

n=int(input("Enter any number "))
for i in range(n,0,-1):
    for j in range(i):
        print('*',end='')
    print()
