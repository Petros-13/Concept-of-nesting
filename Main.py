Attendance=int(input("How many days did you attend class:"))
if Attendance>=75:
    print("You are allowed to take exams")
else:
    Attendance=(input("Were you sick?:"))
    if (Attendance=="Yes" or "yes" or "YES"):
        print("You can take exams")
    else:
        print("You are not allowed to take exams")