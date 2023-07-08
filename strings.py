name = "Sakshi"
print("Hi my name is "+name)

# How will you print this statement in python?: He said, "I want to eat an apple".
# first method
print("He said, \"I want to eat an apple\".")
# second method
print('He said, "I want to eat an apple".')
sentence = "I want to eat an apple"
print(sentence[0:6])
print(len(sentence))
for i in sentence:
    print(i)

# string slicing
sentence = "I want to eat an apple"
print(len(sentence))
print(sentence[:19])
# print(sentence[:len(sentence)-3])
print(sentence[:-3])
# print(22-3)


word = "Apple"
print(word.upper())  # The upper() method converts a string to uppercase.
word = "Apple"
print(word.lower())  # The lower() method converts a string to lowercase.
word = "!!!!!!!Apple!!!!!!!!"
# The strip() method removes any white spaces before and after the string.
print(word.strip('!'))  # op- Apple
# the rstrip() removes any trailing characters.
print(word.rstrip('!'))  # op- !!!!!!!Apple
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
str1 = "Welcome to the Console!!!"
print(str1.center(50, '.'))
str1 = "WelcomeToTheConsole:)"
print(str1.isalnum())

# f-strings
val = 'Geeks'
print(f"{val} for {val} is a portal for {val}")
price = 500.784567
print(f"The salary of {val} engineer is {price:.2f}")
print(
    f"This is how we type a f-string {{val}}, this will print the value in the variable ")


def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)


square(5)
print(square.__doc__)
