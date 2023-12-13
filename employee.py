class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
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


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

