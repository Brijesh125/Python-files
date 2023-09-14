num=[]
div_id=[]
def data():
    test = {
        "device id": "",
        "test time": "",
        "x coordinate": "",
        "y coordinate": "",
        "test name": "",
        "test number": "",
        "upper test limit": "",
        "lower test limit": "",
        "unit": ""
    }
    while True:
        test["device id"] = input("Enter the device id : ")
        if test["device id"].isnumeric() == False and test["device id"].isalnum():
            div_id.append(test["device id"])
            break
        else:
            print("Invalid entry.Try again.")
    while True:
        test["test time"]= input( "Enter test time in the format of (HH:MM): " )
        time=test["test time"]
        if len(time) == 5 and time[2] == ':' and time.replace(':', '').isnumeric():
            break
        else:
            print("Invalid date format.Try again.")
    temp = 1
    while temp:
        try:
            temp = 0
            test["x coordinate"] = float(input("Enter the x coordinate : "))
        except:
            temp = 1
            print("Invalid entry.Try again.")
    temp = 1
    while temp:
        try:
            temp = 0
            test["y coordinate"] = float(input("Enter the y coordinate : "))
        except:
            temp = 1
            print("Invalid entry.Try again.")
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
    print(f"Enter the data of device {i}")
    device[f"device {i}"]=data()
print("test data : ",device)

while True:
    check_id = input("Enter the device id to get details : ")
    if check_id in div_id:
        for i in range(len(div_id)):
            if div_id[i] == check_id:
                print("Data : ",device[f"device {i + 1}"])
        break
    else:
        print("invalid Entry.Enter the correct device id")
while True:
    check_num = input("Enter the test number to get details : ")
    if check_num in num:
        for i in range(len(num)):
            if num[i] == check_num:
                print("Data :",device[f"device {i + 1}"])
        break
    else:
        print("invalid Entry.Enter the correct test number")