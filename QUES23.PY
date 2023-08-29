class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, age):
        result = []
        for emp in self.employees:
            if emp.age == age:
                result.append(emp)
        return result

    def search_by_name(self, name):
        result = []
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                result.append(emp)
        return result

    def search_by_salary(self, operator, salary):
        result = []
        for emp in self.employees:
            if operator == '<' and emp.salary < salary:
                result.append(emp)
            elif operator == '>' and emp.salary > salary:
                result.append(emp)
            elif operator == '<=' and emp.salary <= salary:
                result.append(emp)
            elif operator == '>=' and emp.salary >= salary:
                result.append(emp)
        return result

def main():
    db = EmployeeDatabase()

    emp1 = Employee("161E90", "Raman", 41, 56000)
    emp2 = Employee("161F91", "Himadri", 38, 67500)
    emp3 = Employee("161F99", "Jaya", 51, 82100)
    emp4 = Employee("171E20", "Tejas", 30, 55000)
    emp5 = Employee("171G30", "Ajay", 45, 44000)

    db.add_employee(emp1)
    db.add_employee(emp2)
    db.add_employee(emp3)
    db.add_employee(emp4)
    db.add_employee(emp5)

    print("Search options:")
    print("1. Age\n2. Name\n3. Salary (>, <, <=, >=)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        age = int(input("Enter age to search: "))
        result = db.search_by_age(age)
    elif choice == 2:
        name = input("Enter name to search: ")
        result = db.search_by_name(name)
    elif choice == 3:
        operator = input("Enter operator (<, >, <=, >=): ")
        salary = int(input("Enter salary to compare: "))
        result = db.search_by_salary(operator, salary)
    else:
        print("Invalid choice")
        return

    if result:
        print("\nSearch Results:")
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No matching records found.")

if __name__ == "__main__":
    main()
