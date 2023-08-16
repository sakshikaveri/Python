# '''You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.'''

# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: str
#         """
#         self.word1=word1
#         self.word2=word2
#         merged=''
#         i=0
#         j=0
#         while i<len(word1) and j<len(word2):
#             merged+=word1[i]
#             merged+=word2[j]
#             i+=1
#             j+=1
#         merged+=word1[i:]
#         merged+=word2[j:]

#         return merged


# msg=Solution()
# print(msg.mergeAlternately('ab','pqrs'))


# SAP Practice

'''You’re given a string where multiple characters are repeated consecutively. 
You’re supposed to reduce the size of this string using mathematical logic given as in the example below :'''

# MY SOLUTION


def fun1(message):
    count_a = 0
    count_b = 0
    count_e = 0
    count_f = 0
    count_g = 0
    for i in range(len(message)):
        # print(message[i])
        if message[i] == 'a':
            count_a += 1
        if message[i] == 'b':
            count_b += 1
        if message[i] == 'e':
            count_e += 1
        if message[i] == 'f':
            count_f += 1
        if message[i] == 'g':
            count_g += 1

    print('a'+str(count_a)+'b'+str(count_b)+'e' +
          str(count_e)+'f'+str(count_f)+'g'+str(count_g))


fun1('aabbbbeeeeffggg')
# op= a2b4e4f2g3

# EXPECTED SOLUTION
# def compress_string(message):
#     compressed_message = ""
#     current_char = None
#     current_count = 0

#     for i in range(len(message)):
#         if message[i] == current_char:
#             current_count += 1
#         else:
#             if current_char is not None:
#                 compressed_message += current_char + str(current_count)
#             current_char = message[i]
#             current_count = 1

#     if current_char is not None:
#         compressed_message += current_char + str(current_count)

#     return compressed_message


# compressed_str = compress_string('aaaaayggttth')
# print(compressed_str)


# def fun1(arr):
#     for i in range(len(arr)):
#         value=arr[0]
#         if value>arr[i]:
#             greater_value=value
#             # print("Largest number=",arr[i])
#         else:
#             greater_value=arr[i]
#             # print("Largest number=",greater_value)

#         if arr[i]<value:
#             smallest_number=arr[i]
#             # print("Smallest number=",smallest_number)
#         else:
#             smallest_number=value
#             # print("Smallest number=",value)
#         value=arr[i]
#     return greater_value,smallest_number

# import array
# arr=array.array('i',[0,1,2,3,4,5,9])
# print(fun1(arr))


# a3 + a2b + 2a2b + 2ab2 + ab2 + b3.

# def soln(a, b):
#     sum = ((a+b)**3)
#     return sum


# def check(a, b):
#     sum = a**3 + a**2*b + 2*a**2*b + 2*a*b**2 + a*b**2 + b**3
#     return sum


# # print(2**3)
# print(soln(2, 3))
# print(check(2, 3))


# def dealership1(cars, bikes):
#     return (cars*4) + (bikes*2)


# def dealership2(cars, bikes):
#     return (cars*4) + (bikes*2)


# def dealership3(cars, bikes):
#     return (cars*4) + (bikes*2)


# print("Total number of dealerships: 3")
# print(dealership1(4, 2))
# print(dealership2(4, 0))
# print(dealership3(1, 2))

# Reduce the string by removing K consecutive identical characters
def compressed_str(message):
    compressed_string=''
    counter=0
    current_char=None
    for i in range(len(message)):
        if message[i]==current_char:
            counter+=1
            print(counter)
        else:
            if current_char is not None:
                compressed_string+=current_char+str(counter)
            current_char=message[i]
            counter=1
    if current_char is not None:
            compressed_string+=current_char+str(counter)
    return compressed_string


# print(compressed_str('aaaaayggttth'))
def compressed_str(message):
    compressed_string=''
    current_char=message[0]
    for i in range(1,len(message)):
        # print(message[i])
        if current_char==message[i]:
            compressed_string.replace(message[i],'')
        # print(current_char)
        else:
            compressed_string+=current_char
        current_char=message[i]
        compressed_string=current_char
    return compressed_string

print(compressed_str('geeksforgeeks'))
# op- gksforgks

