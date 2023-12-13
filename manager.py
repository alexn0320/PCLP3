from employee import Employee

#clasa extinde clasa Employee
class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.name = name
        self.salary = salary
        #prefixarea echipei 
        self.department = "A07_" + department
    
        Manager.mgr_count += 1

    #X%3 == 2
    def display_employee(self):
        print("Department: ", self.department)