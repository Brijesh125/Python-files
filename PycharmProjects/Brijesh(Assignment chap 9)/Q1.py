def data():
    employee = {
        "first name": "",
        "last name": "",
        "joining date": "",
        "salary": ""
    }
    while True:
        employee["first name"] = input("Enter the first name: ")
        if employee["first name"].isalpha():
            break
        else:
            print("Invalid entry.Try again.")
    while True:
        employee["last name"] = input("Enter the last name: ")
        if employee["last name"].isalpha():
            break
        else:
            print("Invalid entry.Try again.")
    while True:
        employee["joining date"] = input("Enter Joining Date (DD/MM/YYYY): ")
        date = employee["joining date"]
        if len(date) == 10 and date[2] == '/' and date[5] == '/' and date.replace('/', '').isnumeric():
            break
        else:
            print("Invalid date format.Try again.")
    while True:
        employee["salary"] = input("Enter the salary: ")
        if employee["salary"].isnumeric():
            break
        else:
            print("Invalid entry.Try again.")
    return employee

n=int(input("Enter the number of employees : "))
company={}
for i in range(1,n+1):
    print(f"Enter the data of employee {i}")
    company[f"employee {i}"]=data()
print("employee data : ",company)
