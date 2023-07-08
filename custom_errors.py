# num=int(input("Enter number between 5 and 9: "))
# if (num<5 or num>9):
#     raise ValueError("Value should be between 5 and 9")

# msg=input("Enter a string: ")
# if(msg != 'quit'):
#     raise NameError('The entered string is wrong')

num=input("Enter number between 5 and 9: ")
if(num=='quit'):
    print("User entered quit so quit")
elif (int(num)<5 or int(num)>9):
    raise ValueError("Value should be between 5 and 9")

