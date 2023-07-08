# val=5
# for i in range(1,11):
#     print(val,"x",i,"=",val*i)
#     if i==5:
#         break
# print("Loop ke bahar agaya")

val1=int(input("Enter a number you want to skip between 1 to 10: "))
for i in range(1,11):
    if (i==val1):
        continue
    print(i)

