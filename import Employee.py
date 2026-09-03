from emp_class import Employee
print("Welcome to EMp Application")
emp = Employee()
eid = 121
while True:
    choice = int(input('''Enter your choice
1. Add New Employee
2. Update Salary
3. update exp
4. Get Employee
5. Exit
Enter choice: '''))
    if choice == 1:
        eid += 1
        name = input("Enter name: ")
        salary = int(input("Enter salary: "))
        exp = int(input("Enter exp: "))
        emp.setEmployeeDetails(eid, name, salary, exp)
    elif choice == 2:
        g = input("Enter grade: ")
        if g == 'A':
            increment = 7
        elif g == 'B':
             increment = 8
        elif g == 'C':
            increment = 9
        else:
            print("Invalid grade")
            continue
        print(emp.updateSal(increment))
    elif choice == 3:
        new= int(input("Enter new experience: "))
        print(emp.updex(new))
    elif choice == 4:
        print(emp.getEmployee())
    elif choice == 5:
        print("End of Application")
        break
    else:
        print("Wrong choice")