import time
my_time = time.strftime('%H:%M:%S')
print("The current time is: "+my_time)

hours = int(time.strftime('%H'))
# print(hours)
minutes = int(time.strftime('%M'))
# print(minutes)
seconds = int(time.strftime('%S'))
# print(seconds)

name = input("Please enter your name: ")
if(hours < 12):
    print("Hey", name, ",GOOD MORNING")
elif hours > 12 and hours < 16:
    print("Hey", name, ",GOOD AFTERNOON")
elif hours > 16 and hours < 20:
    print("Hey", name, ",Good Evening")
else:
    print("Hey", name, ",Good Night")
# https://docs.python.org/3/library/time.html#time.strftime

# short hand if-else
a=400
b=50
c=10 if a>b else print("Hi")
print(c)