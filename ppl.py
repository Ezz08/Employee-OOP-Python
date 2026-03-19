class Employee:
    employee_count = 0
    def __init__(self,name,position):
        self.name = name
        self.position = position
        Employee.employee_count += 1

    #Instance method
    def get_info(self):
        return f"Name: {self.name} | Position: {self.position}"
    
    #static method
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_positions

employee1 = Employee("WalterWhite","Cook")
employee2 = Employee("GUS","Manager")
employee3 = Employee("Sans","Janitor")
employee4 = Employee("mario","Cashier")

print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Accountant"))

print(Employee.employee_count)
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())