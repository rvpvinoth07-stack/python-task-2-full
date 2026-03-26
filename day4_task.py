
employees = []

def add_employee():
    name = input("VINOTH")
    age = int(input("30"))
    role = input("DA")
    salary = int(input("30,000"))
    
    emp = {"VINOTH": name, "30": age, "DA": role, "30,000": salary}
    employees.append(emp)
    print("Employee added")

def display():
    for emp in employees:
        print(emp)

def update():
    name = input("Enter name to update: ")
    for emp in employees:
        if emp["name"] == name:
            emp["salary"] = int(input("Enter new salary: "))
            print("Updated")

def delete():
    name = input("Enter name to delete: ")
    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)
            print("Deleted")

while True:
    print("1.Add 2.Display 3.Update 4.Delete 5.Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        display()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        break



students = {}

name = input("Enter student name: ")
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

total = m1 + m2 + m3
avg = total / 3

print("Name:", name)
print("Total:", total)
print("Average:", avg)

if avg >= 75:
    print("Grade: A")
elif avg >= 50:
    print("Grade: B")
else:
    print("Grade: C")


cart = []

while True:
    print("1.Add 2.Remove 3.Display 4.Total 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Product name: ")
        price = int(input("Price: "))
        qty = int(input("Quantity: "))
        cart.append({"name": name, "price": price, "qty": qty})

    elif choice == "2":
        name = input("Enter product to remove: ")
        for item in cart:
            if item["name"] == name:
                cart.remove(item)

    elif choice == "3":
        for item in cart:
            print(item)

    elif choice == "4":
        total = 0
        for item in cart:
            total += item["price"] * item["qty"]
        print("Total Bill:", total)

    elif choice == "5":
        break

