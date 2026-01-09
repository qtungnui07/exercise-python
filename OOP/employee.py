class Employee:
    # Khai báo properties và gán giá trị cho chúng
    def __init__(self, ID = None, salary = 0, department = None):
        self.ID = ID
        self.salary = salary
        self.department = department

# Tạo một object của class Employee với các tham số mặc định
steve = Employee()

# Tạo một object của class Employee với tham số của chúng ta
mark = Employee("3789", 2500, "Human Resources")

# In ra properties của mark và steve
print("Steve")
print("ID :", steve.ID)
print("Salary :", steve.salary)
print("Department :", steve.department)
print("Mark")
print("ID :", mark.ID)
print("Salary :", mark.salary)
print("Department :", mark.department)
