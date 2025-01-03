"""

The marks obtained by a student in 5 different subjects are input through the keyboard. The student gets a division as per the following rules:

Percentage above or equal to 60 - First division

Percentage between 50 and 59 - Second division

Percentage between 40 and 49 - Third division

Percentage less than 40 - Fail

Write a program to calculate the division obtained by the student

"""

english=int(input("Enter the english marks"))
marathi=int(input("Enter the marathi marks"))
hindi=int(input("Enter the hindi marks"))
maths=int(input("Enter the maths marks"))
science=int(input("Enter the science marks"))

total_marks=english+marathi+hindi+maths+science
percentage=total_marks/500*100
print(percentage)

if(percentage>=60):
    print("first division")
elif(percentage>=50):
    if(percentage<59):
        print("Second Division")
    else:
        print("not")
elif(percentage>=40):
    if(percentage<49):
        print("third Division")
    else:
        print("not")
elif(percentage<40):
    print("fail")
