
def greet(fx):
    def mfx(*args,**kwargs):
        print('Good Morning')
        fx(*args,**kwargs)
        print("The function is executed")
    return mfx


@greet
def hello():
    print('Hello')

@greet
def sum(a,b):
    print( a+b)

hello()
sum(3,4)
