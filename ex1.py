from manager import Manager
from employee import Employee

#Exercitiul 1
#X = 5
#Y = 9

def main():
    manager1 = Manager("Manager1", 1000, "HR")
    manager1.display_employee()
    manager2 = Manager("Manager2", 2000, "Inginerie")
    manager2.display_employee()
    manager3 = Manager("Manager3", 3000, "Productie")
    manager3.display_employee()

    emp = Employee("Angajat1", 500)

    print(emp.empCount)
    print(manager1.mgr_count)

if __name__ == '__main__':
    main()