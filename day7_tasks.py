#2
from abc import ABC, abstractmethod
from functools import reduce

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass

class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = int(fees)

    def get_details(self):
        return f"Student: {self.name}, Dept: {self.dept}, Fees: {self.fees}"
    
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = int(salary)

    def get_details(self):
        return f"Faculty: {self.name}, Salary: {self.salary}"
    
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty: {self.name}, Salary: {self.salary}, Duration: {self.duration}"
    

students = [
    Student("vinoth", 1, "IT", 60000),
    Student("arun", 2, "CSE", 45000),
    Student("kumar", 3, "ECE", 70000)
]

faculty = [
    Faculty("raj", 101, 40000),
    Faculty("sita", 102, 25000),
    TempFaculty("john", 103, 35000, "6 months")
]

#3
students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)

#4
student_names = list(map(lambda s: s.name, students))

#5
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

#6
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

#7
def process_users(users, func):
    return list(map(func, users))

print("\n--- All Details ---")
for s in students:
    print(s.get_details())

for f in faculty:
    print(f.get_details())

print("\n--- Sorted Students by Fees ---")
for s in students:
    print(s.name, s.fees)

print("\n--- Filtered Students (Fees > 50000) ---")
for s in high_fee_students:
    print(s.name)

print("\n--- Total Fees ---", total_fees)
print("--- Total Salary ---", total_salary)

print("\n--- Names using Higher Order Function ---")
print(process_users(students, lambda x: x.name))