num=[]
def data():
    test = {
        "test name": "",
        "test number": "",
        "upper test limit": "",
        "lower test limit": "",
        "unit": ""
    }
    while True:
        test["test name"] = input("Enter the test name : ")
        if test["test name"].isnumeric() == False and test["test name"].isalnum():
            break
        else:
            print("Invalid entry.Try again.")
    while True:
        test["test number"] = input("Enter the unique test number : ")
        if test["test number"].isnumeric():
            if test["test number"] not in num:
                num.append(test["test number"])
                break
            else:
                print("Invalid entry.Test number already exists")
        else:
            print("Invalid entry.Try again.")
    temp = 1
    while temp:
        try:
            temp = 0
            test["upper test limit"] = float(input("Enter the upper test limit : "))
        except:
            temp = 1
            print("Invalid entry.Try again.")
    temp = 1
    while temp:
        try:
            temp = 0
            test["lower test limit"] = float(input("Enter the lower test limit : "))
        except:
            temp = 1
            print("Invalid entry.Try again.")
    while True:
        test["unit"] = input("Enter the unit : ")
        if test["unit"].isalpha():
            break
        else:
            print("Invalid entry.Try again.")
    return test
n=int(input("Enter the number of device tests : "))
device={}
for i in range(1,n+1):
    print(f"Enter the test data of device {i}")
    device[f"device {i}"]=data()
print("test data : ",device)