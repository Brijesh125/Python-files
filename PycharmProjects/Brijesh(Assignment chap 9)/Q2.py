def data():
    pin = {
        "pin number": "",
        "pin name": "",
        "pin type": "",
        "Description": ""
    }
    while True:
        pin["pin number"] = input("Enter the pin number: ")
        if pin["pin number"].isnumeric():
            if int(pin["pin number"]) <= 64:
                break
            else:
                print("Invalid entry.Enter pin number less than 65.")
        else:
            print("Invalid entry.Enter pin number less than 65.")
    while True:
        pin["pin name"] = input("Enter the pin name: ")
        if pin["pin name"].isnumeric() == False and pin["pin name"].isalnum():
            break
        else:
            print("Invalid entry.Try again.")
    while True:
        pin["pin type"] = input("Enter the pin type (input,output or bidirectional): ")
        if pin["pin type"] == "input" or pin["pin type"] == "output" or pin["pin type"] == "bidirectional":
            break
        else:
            print("Invalid entry.Enter any of input,output or bidirectional.")
    while True:
        pin["Description"] = input("Enter the pin description: ")
        if pin["Description"].isnumeric() == False and pin["Description"].isalnum():
            break
        else:
            print("Invalid entry.Try again.")
    return pin

n=int(input("Enter the number of devices : "))
device={}
for i in range(1,n+1):
    print(f"Enter the data of device {i}")
    device[f"device {i}"]=data()
print("device data : ",device)