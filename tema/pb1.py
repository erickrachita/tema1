class Employee:
   
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_employee(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

    def __del__(self):
        Employee.empCount -= 1

class Manager(Employee):
 
    mgrCount = 0
    X = 7

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        Manager.mgrCount += 1

    def display_employee(self):
        print("D10")

    def __del__(self):
        Manager.mgrCount -= 1
        super().__del__()

# Crearea Y/3 obiecte ale clasei Manager
Y = 14  
managers = []
for i in range(Y // 3):
    manager_name = f"Manager{i + 1}"
    manager_salary = 50000 + i * 10000
    manager_department = f"D10"
    manager = Manager(manager_name, manager_salary, manager_department)
    managers.append(manager)

# Afișarea informațiilor pentru toate obiectele Manager
print("\nDisplaying Manager Information:")
for manager in managers:
    manager.display_employee()

# Afișarea informațiilor pentru obiectele Employee
print("\nDisplaying Employee Information:")
employee1 = Employee("Employee1", 45000)
employee2 = Employee("Employee2", 48000)
employee1.display_employee()
employee2.display_employee()

# Afișarea empCount pentru o instanță a clasei Employee și pentru una a clasei Manager
print("\nEmployee Count:", employee1.empCount)
print("Manager Count:", manager.mgrCount)
