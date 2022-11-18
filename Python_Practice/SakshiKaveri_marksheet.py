# taking data

name = str(input("Enter the full name of the student "))
roll_no = int(input("Enter the roll number of the student "))
seat_no = int(input("Enter the seat no of the student "))

phy = int(input("\nEnter Physics marks "))
if(phy > 100 or phy < 1):
    print("WARNING!! Enter value between 1 to 100")
    phy = int(input("Enter Physics marks "))

chem = int(input("Enter Chemistry marks "))
if(chem > 100 or chem < 1):
    print("WARNING!! Enter value between 1 to 100")
    phy = int(input("Enter Chemistry marks "))

maths = int(input("Enter Mathematics marks "))
if(maths > 100 or maths < 1):
    print("WARNING!! Enter value between 1 to 100")
    phy = int(input("Enter Mathematics marks "))

# calculating data and printing the data
print("\nDATA OF THE STUDENT")
print("Name of the student:", name)
print("Roll number of the student:", roll_no)
print("Seat number of the student:", seat_no)
print("\nMarks obtained in PHYSICS:", phy)

if phy < 33:
    print("You are fail")
else:
    print("The student has succesfully passed Phyics")

print("Marks obtained in CHEMISTRY:", chem)

if chem < 33:
    print("You are fail")
else:
    print("The student has succesfully passed Chemistry")


print("Marks obtained in MATHEMATICS:", maths)

if maths < 33:
    print("You are fail")
else:
    print("The student has succesfully passed Mathematics")


marks = phy+chem+maths
percent = (marks/300) * 100
print("\nThe percentage obtained by the student is %.2f" % percent, "%")


#print("The total marks obtained out of 300 are",marks)
