class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1

class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

        self.department = "A07_" + self.department
    
        Manager.mgr_count += 1

    def display_employee(self):
        print("Name: ", self.name)



def main():
    manager1 = Manager("David", 1500, "Logistica")
    manager1.display_employee()
    manager2 = Manager("Alex", 2000, "Sport")
    manager2.display_employee()
    manager3 = Manager("Andrei", 4000, "IT")
    manager3.display_employee()

    emp = Employee("Marian", 200)

    print(emp.empCount)
    print(manager1.mgr_count)

if __name__ == '__main__':
    main()
#X = 9
#Y = 10
