from employee import Employee
print("Welcome to EMp Application")

emp=Employee()
eid=121
while True:
    choice=int(input('''Enter your choice 1. Add New Employee 2. Update Salary 3. Get Employee
                 4.Exit'''))
    if choice==1:
        eid+=1
        name=input("Enter name")
        salary=float(input("Enter salary"))
        exp=int(input("Enter exp"))
        emp.setEmployeeDetails(eid,name,salary,exp)

    elif choice==2:
        grade=input("enter grade")
        if grade =="A":
            increment=7
        elif grade == "B":
            increment=5
        elif grade=="c":
            increment=3
        else:
            increment=1
            continue
        print(emp.updateSal(increment))
    elif choice==3:
        new= int(input("Enter new experience: "))
        print(emp.updateexp(new))

    elif choice==4:
        print("End of Application")
        break
    else:
        print("Wrong choice")