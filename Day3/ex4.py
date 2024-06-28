class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        super().__init_subclass__()

class Manager(Employee):
    def __init__(self, name, age, salary,department):
        self.department = department
        super().__init__(name, age, salary)       


class Developer(Employee):
    def __init__(self, name, age, salary,programming_language):
        self.programming_language = programming_language
        super().__init__(name, age, salary)


class Company():

    employee_list = []
    manager_list = []
    developer_list = []

    @classmethod
    def add_employee(cls,emp,type):   
        if type == "Manager":
            cls.manager_list.append(emp)
            cls.employee_list.append(emp)
            print(f"\nEmployee {emp.name} added sucessfully!\n")
        if type == "Developer":
            cls.developer_list.append(emp)
            cls.employee_list.append(emp)
            print(f"\nEmployee {emp.name} added sucessfully!\n")


    @classmethod
    def display_employee(cls):
        if cls.employee_list == []:
            print("No available employees, add some!")        

        for manager in cls.manager_list:
            print(f"{manager.name}, a {manager.age} year old, in the {manager.department} with a Salary of {manager.salary}\n")
        for developer in cls.developer_list:
            print(f"{developer.name}, a {developer.age} year old, in the {developer.programming_language} with a Salary of {developer.salary}\n")
        
    @classmethod
    def calculate_salary(cls):
        total_salary = 0
        for employee in cls.employee_list:
            total_salary += employee.salary
        return total_salary


def main():
    choice = int(input("\nWelcome to Estarta Solutions Employee Management System\nWhat task would you like to perform?\n \n1. Add a new employee\n2. Display employees\n3. Calculate total salary\n4. Exit\n\n"))
    
    while (not choice == 4):
        if choice < 1 or choice > 4:
            choice = int(input("Invalid option, please input a value between 1 and 4: "))
               
        if choice == 1:
            type = input("Enter employee type (Manager/Developer): ")
            name = input("Enter employee name: ")
            age = input("Enter employee age: ")
            salary = int(input("Enter employee salary: "))
            
            if type == "Manager":
                dept = input("Enter employee department: ")
                manager_1 = Manager(name,age,salary,dept)
                Company.add_employee(manager_1,type)
            elif type == "Developer":
                prglang = input("Enter employee programming language: ")
                developer_1 = Developer(name,age,salary,prglang)
                Company.add_employee(developer_1,type)
            else:
                print("Invalid type, please try again!\n")

            choice = int(input("\nWhat task would you like to perform?\n \n1. Add a new employee\n2. Display employees\n3. Calculate total salary\n4. Exit\n\n"))

        if choice == 2:
            Company.display_employee()
            choice = int(input("\nWhat task would you like to perform?\n \n1. Add a new employee\n2. Display employees\n3. Calculate total salary\n4. Exit\n\n"))

        if choice == 3:
            print(f"The total Salary of all employees is: {Company.calculate_salary()}\n")
            choice = int(input("\nWhat task would you like to perform?\n \n1. Add a new employee\n2. Display employees\n3. Calculate total salary\n4. Exit\n\n"))
    
    if choice == 4:
        return print("Thank you for using Estarta Solutions Employee Management System.\nGoodbye!\n")
    

        
main()
