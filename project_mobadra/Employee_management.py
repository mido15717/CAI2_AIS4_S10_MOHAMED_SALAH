import csv

# the name of the file
filename = 'employees.csv'


# Employee class
class Employee:
    # constructor that takes the employee details
    def __init__(self, emp_id, name, email, salary, position):
        self.id = emp_id
        self.name = name
        self.email = email
        self.salary = salary
        self.position = position

    # Update method
    def update(self, name=None, email=None, salary=None, position=None):
        self.name = name2
        self.email = email
        self.salary = salary
        self.position = position

    # display method
    def display(self):
        return {
            'ID': self.id,
            'Name': self.name,
            'Email': self.email,
            'Salary': self.salary,
            'Position': self.position
        }


class EmployeeManager:
    # constructor
    def __init__(self):
        self.employees = {}
        self.load_data()

    # load method that reads the data
    def load_data(self):
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employee_name = row['Name']
                    self.employees[employee_name] = {
                        'Email': row['Email'],
                        'Salary': int(row['Salary']),
                        'ID': int(row['ID']),
                        'Position': row['Position']
                    }
        except FileNotFoundError:
            print("No previous employee data found, starting fresh.")

    # saving method that write data into csv file
    def save_data(self):
        with open(filename, mode='w', newline='') as file:
            fieldnames = ['Name', 'Email', 'Salary', 'ID', 'Position']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for employee_name, details in self.employees.items():
                writer.writerow({
                    'Name': employee_name,
                    'Email': details['Email'],
                    'Salary': details['Salary'],
                    'ID': details['ID'],
                    'Position': details['Position']
                })

    # add employee method that takes the personal details of the employee
    def add_employee(self):
        employee_name = input("enter the name of the employee: ")
        if employee_name not in self.employees:
            employee_email = input("enter employee email: ")
            try:
                employee_salary = int(input("enter employee salary: "))
                employee_id = int(input("enter employee ID: "))
                for ID in self.employees.values():
                    if ID['ID'] == employee_id:
                        print("the ID already exists. Please try again.")
                        return
            except ValueError:
                print("try again with an integer")
                return

            employee_poss = input("enter the position of the employee: ")
            self.employees[employee_name] = {'Email': employee_email, 'Salary': employee_salary, 'ID': employee_id,
                                             'Position': employee_poss}
            print(f"employee '{employee_name}' added successfully")
            self.save_data()

        elif employee_name in self.employees:
            print(f"employee '{employee_name}' is already added")
        else:
            print("invalid name")

    # delete method that deletes the employee from the csv file based on there ID
    def delete_employee(self):
        emp = int(input("enter the ID of the employee you want to delete:"))
        for employe, details in self.employees.items():
            if details['ID'] == emp:
                del self.employees[employe]
                print("employee is deleted")
                self.save_data()
                break

    # modify employee method that modifies the personal details of an employee based on there ID
    def modify_employee(self):
        emp_id = int(input("Enter the ID of the employee you want to modify: "))
        for name, details in self.employees.items():
            if details['ID'] == emp_id:
                print(f"Current details: {name}, {details['Email']}, {details['Salary']}, {details['Position']}")
                email = input("Enter new email: ")
                salary_input = input("Enter new salary: ")
                salary = int(salary_input) if salary_input else details['Salary']
                position = input("Enter new position: ")

                if email:
                    details['Email'] = email
                details['Salary'] = salary
                if position:
                    details['Position'] = position

                print(f"Employee '{name}' updated successfully.")
                self.save_data()
                return
        print("No employee found with that ID.")

        # search employee method that returns the personal details of an employee based on ID

    def search_emp(self):
        if not self.employees:
            print("there is no valid employees")
        else:
            emp = int(input("enter the ID of the employee you want:"))
            for employe, details in self.employees.items():
                if details['ID'] == emp:
                    print(f"Name: {employe}")
                    print(f"  Email: {details['Email']}")
                    print(f"  Salary: {details['Salary']}")
                    print(f"  Position: {details['Position']}")

    # display method
    def display_all(self):
        if not self.employees:
            print("there is no valid employees")
        else:
            for employees, details in self.employees.items():
                print(f"Name: {employees}")
                print(f"  Email: {details['Email']}")
                print(f"  Salary: {details['Salary']}")
                print(f"  ID: {details['ID']}")
                print(f"  Position: {details['Position']}")


# defining an object of EmployeeManager
employees = EmployeeManager()

# Command-Line Interface
while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Delete Employee")
    print("4. Search for an Employee")
    print("5. Modify Employee")
    print("0. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        employees.add_employee()
    elif choice == 2:
        employees.display_all()
    elif choice == 3:
        employees.delete_employee()
    elif choice == 4:
        employees.search_emp()
    elif choice == 5:
        employees.modify_employee()
    elif choice == 0:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")