

print("\n\n\n.......................WELCOME TO SAKSHI'S LIBRARY..........................\n")

print("THESE ARE THE BOOKS AVAILABLE IN OUR LIBRARY:\n")

# defining a dictionary with the list of books and their book-ids available in the library

# NOTEE-->> the book-ids are the keys and the book names are the values


# defining a dictionary with the list of books and their book-ids available in the library

print("The sequence-->  Book-Ids : Book-names\n\n ")
Books_available = {
    'A1234': 'The Diary of a young girl',
    'B5678': 'To Kill a Mockingbird',
    'C2233': '1984',
    'D5679': 'Charlotte’s Web',
    'E3542': 'The Kite Runner',
    'F3456': 'The Grapes of Wrath',
    'G9342': 'Lord of the Flies',
    'H3256': 'Of Mice and Men',
    'W1453': 'A Tale of Two Cities',
    'K5566': 'Romeo and Juliet'
}
print(Books_available)
print('\n')
 

# taking the input from the user for the book they want
book = str(input("Enter the book-id you want: "))
print('\n')


# Here we would be using the nested dictionary method
main = {
    "A1234": {
        'Name': "The Diary of a young girl",
        'Description': "a Jewish teenager who chronicled her family's two years (1942–44) in hiding during the German occupation of the Netherlands during World War II.",
        'Author': 'Anne Frank',
        'book_id': 'A1234',
    },
    "B5678": {
        'Name': "To Kill a Mockingbird",
        'Description': "This book discusses human behavior and the collective conscience of The Deep South during the 20th century. This book discusses hypocrisy, prejudice, hatred, love and innocence with humor.",
        'Author': "Harper Lee",
        'book_id': 'B5678'
    },
    "C2233": {
        'Name': '1984',
        'Description': "1984 is George Orwell’s dystopian and totalitarian world where fear, control and lies take over the lives of people. Look into the life of Winston Smith who struggles with his nature in a world where free will, individuality, and love are not allowed.",
        'Author': "George Orwell",
        'book_id': 'C2233'
    },
    'D5679': {
        'Name': 'Charlotte’s Web',
        'Description': 'Here, you will meet Charlotte, an adorable spider, as well as Fern, a farmer’s daughter. Watch the two try to save Wilbur the piglet from being killed. This book is such a compelling reminder to marvel at the simple wonders of life and to love all living creatures.',
        'Author': 'E.B. White',
        'book_id': 'D5679'
    },
    "E3542": {
        'Name': "The Kite Runner",
        'Description': "The Kite Runner tells the story of a one-of-a-kind friendship. It centers on Amir who tries to find the only friend he’s ever had who previously abandoned him because of the ethnic and religious differences that happened in Kabul, Afghanistan.",
        'Author': "Khaled Hosseini",
        'book_id': 'E3542'
    },
    'F3456': {
        'Name': 'The Grapes of Wrath',
        'Description': 'The Grapes of Wrath centers on an Oklahoma family who is forced to travel to California. Here, you will get to see America as it is divided into the haves and have-nots, as well as the powerful and the powerless.',
        'Author': 'John Steinbeck',
        'book_id': 'F3456'
    },
    'G9342': {
        'Name': 'Lord of the Flies',
        'Description': 'The Lord of the Flies is a classic novel that follows boys that are marooned on an island. Here, they regress into becoming savages, and their joyful island existence turns into a cruel nightmare.',
        'Author': 'William Golding',
        'book_id': 'G9342'
    },
    'H3256': {
        'Name': 'Of Mice and Men',
        'Description': 'Of Mice And Men tells the complex story of a friendship between George Milton and Lennie Small, two migrant workers in California. Here, their bond strengthens as their work towards their dreams of owning their land and pets.',
        'Author': 'John Steinbeck',
        'book_id': 'H3256'
    },
    'W1453': {
        'Name': 'A Tale of Two Cities',
        'Description': 'In this novel, you will get to know Dr Manette, an eighteen years political prisoner as he is released and returns to England with Lucie, his daughter. Here, two men fall in love with Lucie and they become entwined in a story of love and sacrifice.',
        'Author': 'Charles Dickens',
        'book_id': 'W1453'
    },
    'K5566': {
        'Name': 'Romeo and Juliet',
        'Description': 'Romeo and Juliet by William Shakespeare is a tragedy that centers on the joy of young love, and the complexity of revenge.',
        'Author': 'William Shakesphere',
        'book_id': 'K5566'
    }
}

# to display the details of the book that the user has chosen

print("The book you have chosen is: ", main[book])
print('\n ENJOY YOUR READING!!')

print('\n')


# AFTER THE USER HAS CHOSEN THE BOOK, THE BOOK WILL BE REMOVED FROM THE LIST
# OF AVAILABLE BOOKS

# here will use the pop method to remove the book mentioned

print("\n\nThe book with id", book, "will be removed!!!!\n")
Books_available.pop(book)
print("NOW THE BOOKS AVAIABLE ARE: ")
print(Books_available)
print('\n\n')


# FOR CUSTOMER 2
book2 = str(input("Enter the book-id you have chosen "))
print('\n')

print("The book you have chosen is: ", main[book2])
print('\n .....ENJOY YOUR READING!!.....')
print('\n')

print("\n\nThe book with id", book2, "will be removed!!!!\n")
Books_available.pop(book2)
print("NOW THE BOOKS AVAIABLE ARE: ")
print(Books_available)
print('\n\n')

# if we want to add a new book to our books available collection we can do so by using 2 methods

print("A new stock has arrived in the library with 3 new books's stocks\n, ")

# so now the list of available books will be updated


print("NEW STOCK!!!")
Books_available['F6767'] =  'The Book Thief'              # 1st method
Books_available['G8899'] = 'The Catcher in the Rye'       # 1st method
Books_available.update({'H9900': 'The Lion, the Witch'} ) # second method using update()
print(Books_available)
print('\n\n')

# OPTIONAL TASKS

# if you want to display only specific value in a nested dictionary then

print("Directly printing the values: \n")
print('NAME- ',main[book]['Name'])
print('DESCRIPTION- ',main[book]['Description'])
print('AUTHOR-',main[book]['Author'])
print('Book-id-',main[book]['book_id'])

print("\n\n..............THANKYOU FOR VISITING THIS LIBRARY!!!...................\n\n")

