'''Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.'''

# List1 is for storing question
list1 = ['''What is the capital of India?''',
         '''a) Delhi'''
         ''' b)Punjab'''
         ''' c)Uttarakhand'''
         ''' d)Bijapur''']
real = 'a'
print(list1)
ans = input("Enter your option: ")
if(ans != 'a' or 'b' or 'c' or 'd'):
    print("Enter valid option")
if (ans == real):
    print('CONGARTULATIONS!!!!!')
    print('You have answered correctly and won a cash prize of Rs\'50,000\'')
list2 = []
