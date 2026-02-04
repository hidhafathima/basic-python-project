print("Welcome to student grade Manangemnet system")
mark1=int(input("Enter the mark of maths"))
mark2=int(input("Enter the mark of physics"))
mark3=int(input("Enter the mark of chemistry"))
mark4=int(input("Enter the mark of english"))
mark5=int(input("Enter the mark of hindi"))
total=mark1+mark2+mark3+mark4+mark5
avg=total/5

if avg>=90:
    grade='A'
elif avg>=75:
    grade='B'
elif avg>=60:
    grade='C'
elif avg>=40:
    grade='D'
else:
    grade='Fail'
print("\n----- RESULT -----")
print("Total Marks:",total)
print("Average Marks:",avg)
print("Grade:",grade)
