# Write a Python program that rotates an array by two positions to the right.

# a=[1,2,3,4]
# # output=[3,4,1,2]
# print(a)
# output_list=[]
# for i in range(len(a)-2,len(a)):
#     output_list.append(a[i])
# for i in range(0,len(a)-2):
#     output_list.append(a[i])

# print("After rotation:")
# print(output_list)

# Write a Python code to reverse a given list.

# a=[25,30,35,40]
# output=[]
# output.append(a[len(a)-1])
# # for i in range(4,):
# #     output.append(a[i])
# # print(output)
# for i in range(0,len(a)-1):
#     output.append(a[i])
# print(output)

# Write a Python program that removes vowels from a string.

# msg='Sakshi'
# output=''
# for i in msg:
#     if i in ('a','e','i','o','u'):
#         i=''
#     output=output+i
# print(output)

# Compute the LCM of two given numbers using Python code.

# a=24
# b=92
# if a>b:
#     greater=a
# else:
#     greater=b

# while(True):
#     if ((greater%a==0)and(greater%b==0)):
#         lcm=greater
#         break
#     greater=greater+1

# print('The LCM would be',greater)

#  Using the Iterative technique, calculate factorial in Python.

# 4!= 4x3x2x1
# using Recursion
# def num(n):
#     if n==0 or n==1:
#         return 1
    
#     return n *(num(n-1))

# print(num(4))


# palindrome
# Creating a string  
# sequence = 'sakshi' 
# # Reversing the string  
# reverse = sequence[::-1]  
# print(reverse)
  
# # Checking if the string is a palindrome  
# if reverse == sequence:  
#     print("The sequence is a palindrome")  
# else:  
#     print("The sequence is not a palindrome")  

# Prime number
# num=34
# for i in range(2,num):
#     if num%i==0:
#         print("The number is not a prime number")
#         break
#     else:
#         print("The number is a prime number")

class Solution(object):
    def isValid(self, s):
        output=''
        for i in range(len(s)):
            # print(s[i])
            if '(' or ')' or '{' or '}' or '[' or ']' in s:
                output+=s[i]
                break
            if s[i] in output:
                output+=s[i]
                return 'true'
            else:
                return 'false'
  
obj1=Solution()
print(obj1.isValid('(]'))
