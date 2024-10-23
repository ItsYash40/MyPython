'''
factorial(0)=1
factorial(1)=1
factorial(2)=2x1
factorial(3)=3x2x1

factorial(n)=nx(n-1)x(n-2)x... x 3x2x1
factorial(n)=n x factirial(n-1)

'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n=int(input("Enter a nunber: "))
print(f"The factorial of this number is: {factorial(n)}")