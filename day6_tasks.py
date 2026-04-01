#1
class User:
    users_count = 0

    def __init__(self, user_name="", pwd=""):
        self.__user_name = user_name
        self.__pwd = pwd
        User.users_count += 1

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"Registering user: {self.__user_name}")
        return self

    def login(self):
        print(f"Logging in: {self.__user_name}")
        return self

    def greet(self):
        print("Welcome User")
        return self


print("")
user1 = User()
user1.set_user("john", "john@123")
user1.register()
user1.login()
print("Username only:", user1.get_user())


#2
class Student(User):
    def student_greet(self):
        print("Hello Student")

    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")

    def greet(self):
        print("Welcome Faculty")
        return self


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")

print("\n")
student = Student("arun", "stu123")
faculty = Faculty("meena", "fac123")
temp_faculty = TempFaculty("ravi", "temp123")

student.register()
student.login()
student.student_greet()

faculty.register()
faculty.login()
faculty.faculty_greet()

temp_faculty.register()
temp_faculty.login()
temp_faculty.faculty_greet()
temp_faculty.tempFaculty_greet()

print("\nParent cannot access child-only methods.")
parent_user = User("parent", "pass")

#3
print("\n")
user2 = User("base_user", "123")
student2 = Student("kumar", "456")
faculty2 = Faculty("divya", "789")

user2.greet()
student2.greet()
faculty2.greet()

#4
print("\n")


class ChainUser:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


chain_user = ChainUser()
chain_user.login().greet().register()

print("\n")


class MiniUser:
    users_count = 0

    def __init__(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd
        MiniUser.users_count += 1

    def get_user(self):
        return self.__user_name

    def login(self):
        print(f"{self.__user_name} logged in")
        return self

    def register(self):
        print(f"{self.__user_name} registered")
        return self

    def greet(self):
        print("Welcome User")
        return self


class MiniStudent(MiniUser):
    def greet(self):
        print("Welcome Student")
        return self


class MiniFaculty(MiniUser):
    def greet(self):
        print("Welcome Faculty")
        return self


mini_student = MiniStudent("vicky", "111")
mini_faculty = MiniFaculty("anita", "222")

mini_student.login().greet().register()
mini_faculty.login().greet().register()

print("Total users created:", MiniUser.users_count)
print("Total users created in User hierarchy:", User.users_count)

