
phy = int(input("\nEnter Physics marks "))
if(phy > 100 or phy < 1):
    print("WARNING!! Enter value between 1 to 100")
    phy = int(input("Enter Physics marks "))

chem = int(input("Enter Chemistry marks "))
if(chem > 100 or chem < 1):
    print("WARNING!! Enter value between 1 to 100")
    chem = int(input("Enter Chemistry marks "))

maths = int(input("Enter Mathematics marks "))
if(maths > 100 or maths < 1):
    print("WARNING!! Enter value between 1 to 100")
    maths = int(input("Enter Mathematics marks "))

marks = phy+chem+maths
print("\nTotal marks obtained out of 300:", marks)
percent = (marks/300)*100
print("The percentage obtained by the student is %.2f" % percent, "%")

if percent >= 90 and percent <= 100:
    print("A GRADE--> EXCELLENT")
elif percent >= 80:
    print("B GRADE")
elif marks >= 70:
    print("C GRADE")
elif marks >= 60:
    print("C GRADE")
else:
    print("FAIL")
