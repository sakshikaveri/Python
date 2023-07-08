a=[1,2,3,4,5]
for index,mark in enumerate(a):
    print(mark)
    if(index==3):
        print("The value previously was 4")

a=[1,2,3,4,5]
for index,mark in enumerate(a,start=1):
    print(mark)
    if(index==3):
        print("The value previously was 3")

a=[1,2,3,4,5]
for index,mark in enumerate(a,start=1):
    print(index,mark)
    if(index==3):
        print("The value previously was 3")
