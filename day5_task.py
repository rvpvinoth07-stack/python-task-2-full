#1
def create_user(name, age, role):
    return {
        "name": name.title(),
        "age": age,
        "role": role
    }

users = []
users.append(create_user("vinoth", 25, "developer"))
users.append(create_user("kumar", 28, "analyst"))

print("User List:")
for user in users:
    print(user)

#2
def calculate_total(*numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average

total, average = calculate_total(10, 20, 30, 40)
print("\nTask 2: Calculator")
print("Total:", total)
print("Average:", average)

#3
def system_config(**settings):
    print("\nSystem Config:")
    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0")

#4
def factorial(n):
    if n < 0:
        return "Error: Negative number"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("\nFactorial:", factorial(5))
print("factorial(0):", factorial(0))
print("factorial(-2):", factorial(-2))

#5
def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

square_list = [i * i for i in range(1, 6)]
square_gen = square_generator(5)

print("\nList vs Generator")
print("List:", square_list)
print("List type:", type(square_list))
print("Generator type:", type(square_gen))

print("Generator values:")
for value in square_gen:
    print(value)

#6
print("\nException Handling")
try:
    num = int(input("\nEnter numerator: "))
    den = int(input("Enter denominator: "))
    result = num / den
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input")
finally:
    print("Program Completed")

#7
print("\nFile Handling")
file = open("team_data.txt", "w")
for user in users:
    file.write(f"Name: {user['name']}, Age: {user['age']}, Role: {user['role']}\n")

file = open("team_data.txt", "r")
print("\nFile Content:")
print(file.read())

print("File closed before closing?:", file.closed)
file.close()
print("File closed after closing?:", file.closed)

print("File closed after with block?:", file.closed)