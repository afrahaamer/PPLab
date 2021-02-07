def isPrime(n):
    flag = 0
    for i in range(2,n):
        if(n%i!=0):
            flag = 0
        else:
            flag = 1
            break
    if flag == 0: 
        print(n)

lower = int(input("lower limit = "))
upper = int(input("upper limit = "))
print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper+1):
    if num != 1:
        isPrime(num)

