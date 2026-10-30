class Employee:
    def __init__(self,name,employee_id,basic_salary):
        self.name = name
        self.employee_id = employee_id
        self.basic_salary = basic_salary

    def display_details(self):
        print(f"Employee name: {self.name}")
        print(f"Employee ID: {self.employee_id}")

    def calculate_salary(self):
        return self.basic_salary

class Developer(Employee):
    def __init__(self,name,employee_id,basic_salary,programming_language):
        super().__init__(name,employee_id,basic_salary)
        self.programming_language = programming_language

    def display_developer_details(self):
        print(f"Employee name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Basic salary: {self.basic_salary}")
        print(f"Programming language: {self.programming_language}")
        print(f"Final salary: {self.basic_salary+(self.basic_salary/10)}")

developer = Developer("Hemanth","E543",45000,"Python")
developer.display_details()
developer.display_developer_details()