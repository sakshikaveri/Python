num1=int(input("Enter something: "))
print("Does this sentence get executed?")
# if we enter any string value it will throw error and the execution stops there only

try:
    num=int(input("Enter a number: "))
    # print("Good!!!!")
    a=[6,3]
    print(a[num])
except ValueError:
    print("The number entered is not an integer!!")
except IndexError:
    print("Index error")

print("Even after getting error, this sentence will be executed")

# ----------------Finally keyword--------------

# case-1
try:
    num=int(input("Enter a number: "))
    # print("Good!!!!")
    a=[6,3]
    print(a[num])
except ValueError:
    print("The number entered is not an integer!!")
except IndexError:
    print("Index error")

print("Even after getting error or not, this sentence will be executed")

# case-2
try:
    num=int(input("Enter a number: "))
    # print("Good!!!!")
    a=[6,3]
    print(a[num])
except ValueError:
    print("The number entered is not an integer!!")
except IndexError:
    print("Index error")
finally:
    print("Even after getting error or not, this sentence will be executed")

    # dono ke bich me fir difference kya h?
# answer-
def fun1():
    try:
        num=int(input("Enter a number: "))
        return 1
    except ValueError:
        print("The number entered is not an integer!!")
        return 0
    print("Even after getting error, this sentence will be executed")
# yahape print statement execute nai hoga in functions
x=fun1()
print(x)

def fun1():
    try:
        num=int(input("Enter a number: "))
        return 1
    except ValueError:
        print("The number entered is not an integer!!")
        return 0
    finally:
        print("Even after getting error, this sentence will be executed")

x=fun1()
print(x)
