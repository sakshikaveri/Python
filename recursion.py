# # FACTORIAL
# def factorial(n):
#     '''takes an input number from user, to calculate the factorial
#     if n=0 or n=1, the factorial is 1
#     but if any other number, here for eg: 3
#     it will be 3*2*1'''
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(3))
# print(factorial.__doc__)

# 3*factorial(2)
# 3*2*factorial(1)
# 3*2*1

# FIBONACCI SERIES
'''f0=0
f1=1
f2=f1+f0
fn=f(n-1)+f(n-2)
5= 0+1+2+3+4'''
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+fibonacci(n-1)
print(fibonacci(4))