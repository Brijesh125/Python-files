# import random
# possible_number_of_outcomes=int(input("Enter the possible number of outcomes : "))
# next_bike=[random.choice(['RC 390','DUKE 390','DOMINAR 400']) for outcome in range(possible_number_of_outcomes)]
# bike_occurrence={bike:next_bike.count(bike) for bike in next_bike}
# max_occurrence=max(list(bike_occurrence.values()))
# for bike,number_of_occurrence in bike_occurrence.items():
#     if number_of_occurrence==max_occurrence:
#         print(f"Out of {possible_number_of_outcomes} possible outcomes, the probability of me choosing the {bike} as my next bike is {number_of_occurrence}")
#         break



#1

# i=97
# while i<=122:
#     print(chr(i))
#     i=i+1

# 2

# letter=input("Enter the letter : ")
# dec=ord(letter)
# if dec >=65 and dec <=90:
#     print("upper case")
# elif dec >=97 and dec <=122:
#     print("lower case")
# else:
#     print("not a letter")

# 3

# letter=input("Enter the letter : ")
# dec=ord(letter)
# print(chr(dec-32)) if dec >=97 and dec <=122 else print("invalid entry")

# 4

# letter=input("Enter the letter : ")
# dec=ord(letter)
# print(chr(dec+2)) if dec <=125 else print("invalid entry")


def binary(num):
    lis = []
    for i in range(16):
        rem = num % 2
        num = num // 2
        lis.append(rem)
    lis.reverse()
    return lis
#1

# num=int(input("Enter the number : "))
# binary=binary(num)
# print("Binary : ",end="")
# for i in binary:
#     print(i,end="")
# print("\r")
# binary[-12]=1 if binary[-12]==0 else 0
# print("flipped binary : ",end="")
# for i in binary:
#     print(i,end="")

#2

# num=int(input("Enter the number : "))
# binary=binary(num)
# print("Binary : ",end="")
# for i in binary:
#     print(i,end="")
# print("\r")
# print("last four bits : ",end="")
# for i in binary[:4]:
#     print(i,end="")
# print("\r")
# dec=0
# for i in range(len(binary[:4])):
#     dec=dec+binary[i]*2**(len(binary[:4])-1-i)
# print("Decimal value of last four bits = ",dec)

# 3

# num=int(input("Enter the number : "))
# binary=binary(num)
# print("Binary : ",end="")
# for i in binary:
#     print(i,end="")
# print("\r")
# print("7 to 15 bits : ",end="")
# for i in binary[:9]:
#     print(i,end="")
# print("\r")
# dec=0
# for i in range(len(binary[:9])):
#     dec=dec+binary[i]*2**(len(binary[:9])-1-i)
# print("Decimal value of 7 t0 15 bits = ",dec)

#4

# num1=int(input("Enter the 1st number : "))
# num2=int(input("Enter the 2nd number : "))
# binary1=binary(num1)
# binary2=binary(num2)
# print("Binary of num1: ",end="")
# for i in binary1:
#     print(i,end="")
# print("\r")
# print("Binary of num2 : ",end="")
# for i in binary2:
#     print(i,end="")
# print("\r")
# print("Binary of result : ",end="")
# result=binary2[:8]+binary1[8:]
# for i in result:
#     print(i,end="")

# 5

# num1=int(input("Enter the 1st number : "))
# num2=int(input("Enter the 2nd number : "))
# binary=binary(num1)
# print("Binary of num1: ",end="")
# for i in binary:
#     print(i,end="")
# print("\r")
# print(f"bit at position {num2} :",binary[-num2-1])

# 6

# num=int(input("Enter the number : "))
# binary=binary(num)
# print("Binary : ",end="")
# for i in binary:
#     print(i,end="")
# print("\r")
# print("Power of two") if binary.count(1)==1 else print("Not a power of two")

#3

# N=int(input("Enter the number : "))
# f=1
# for i in range(1,N+1):
#     f=f*i
# print(f"Factorial of {N} =",f)

# 4

# first_input=int(input("Enter the 1st input : "))
# if first_input==0:
#     second_input=int(input("Enter the square side : "))
#     print("area =",second_input**2)
# elif first_input==1:
#     second_input=int(input("Enter the triangle base : "))
#     third_input=int(input("Enter the triangle height : "))
#     print("area =",.5*second_input*third_input)
# elif first_input==2:
#     second_input=int(input("Enter the rectangle length : "))
#     third_input=int(input("Enter the rectangle breadth : "))
#     print("area =",second_input*third_input)
# else:
#     print("invalid entry")

#5

# def binary(num):
#     lis = []
#     for i in range(8):
#         rem = num % 2
#         num = num // 2
#         lis.append(rem)
#     lis.reverse()
#     return lis
# reg_value=int(input("Enter the decimal register value : "))
# reg_value=binary(reg_value)
# print("Binary of register value : ",end="")
# for i in reg_value:
#     print(i,end="")
# print("\r")
# if reg_value[-4:-2] == [0,0]:
#     print("The drive is Medium")
# elif reg_value[-4:-2] == [0,1]:
#     print("The drive is Low")
# elif reg_value[-4:-2] == [1,0]:
#     print("The drive is High")
# else:
#     print("The drive is off")



# def data():
#     employee = {
#         "first name": "",
#         "last name": "",
#         "joining date": "",
#         "salary": ""
#     }
#     while True:
#         employee["first name"] = input("Enter the first name: ")
#         if employee["first name"].isalpha():
#             break
#         else:
#             print("Invalid entry.Try again.")
#     while True:
#         employee["last name"] = input("Enter the last name: ")
#         if employee["last name"].isalpha():
#             break
#         else:
#             print("Invalid entry.Try again.")
#     while True:
#         employee["joining date"] = input("Enter Joining Date (DD/MM/YYYY): ")
#         date = employee["joining date"]
#         if len(date) == 10 and date[2] == '/' and date[5] == '/' and date.replace('/', '').isnumeric():
#             break
#         else:
#             print("Invalid date format.Try again.")
#     while True:
#         employee["salary"] = input("Enter the salary: ")
#         if employee["salary"].isnumeric():
#             break
#         else:
#             print("Invalid entry.Try again.")
#     return employee
#
# n=int(input("Enter the number of employees : "))
# company={}
# for i in range(1,n+1):
#     print(f"Enter the data of employee {i}")
#     company[f"employee {i}"]=data()
# print("employee data : ",company)


# def data():
#     pin = {
#         "pin number": "",
#         "pin name": "",
#         "pin type": "",
#         "Description": ""
#     }
#     while True:
#         pin["pin number"] = input("Enter the pin number: ")
#         if pin["pin number"].isnumeric():
#             if int(pin["pin number"]) <= 64:
#                 break
#             else:
#                 print("Invalid entry.Enter pin number less than 65.")
#         else:
#             print("Invalid entry.Enter pin number less than 65.")
#     while True:
#         pin["pin name"] = input("Enter the pin name: ")
#         if pin["pin name"].isnumeric() == False and pin["pin name"].isalnum():
#             break
#         else:
#             print("Invalid entry.Try again.")
#     while True:
#         pin["pin type"] = input("Enter the pin type (input,output or bidirectional): ")
#         if pin["pin type"] == "input" or pin["pin type"] == "output" or pin["pin type"] == "bidirectional":
#             break
#         else:
#             print("Invalid entry.Enter any of input,output or bidirectional.")
#     while True:
#         pin["Description"] = input("Enter the pin description: ")
#         if pin["Description"].isnumeric() == False and pin["Description"].isalnum():
#             break
#         else:
#             print("Invalid entry.Try again.")
#     return pin
#
# n=int(input("Enter the number of devices : "))
# device={}
# for i in range(1,n+1):
#     print(f"Enter the data of device {i}")
#     device[f"device {i}"]=data()
# print("device data : ",device)

# num=[]
# def data():
#     test = {
#         "test name": "",
#         "test number": "",
#         "upper test limit": "",
#         "lower test limit": "",
#         "unit": ""
#     }
#     while True:
#         test["test name"] = input("Enter the test name : ")
#         if test["test name"].isnumeric() == False and test["test name"].isalnum():
#             break
#         else:
#             print("Invalid entry.Try again.")
#     while True:
#         test["test number"] = input("Enter the unique test number : ")
#         if test["test number"].isnumeric():
#             if test["test number"] not in num:
#                 num.append(test["test number"])
#                 break
#             else:
#                 print("Invalid entry.Test number already exists")
#         else:
#             print("Invalid entry.Try again.")
#     temp = 1
#     while temp:
#         try:
#             temp = 0
#             test["upper test limit"] = float(input("Enter the upper test limit : "))
#         except:
#             temp = 1
#             print("Invalid entry.Try again.")
#     temp = 1
#     while temp:
#         try:
#             temp = 0
#             test["lower test limit"] = float(input("Enter the lower test limit : "))
#         except:
#             temp = 1
#             print("Invalid entry.Try again.")
#     while True:
#         test["unit"] = input("Enter the unit : ")
#         if test["unit"].isalpha():
#             break
#         else:
#             print("Invalid entry.Try again.")
#     return test
# n=int(input("Enter the number of device tests : "))
# device={}
# for i in range(1,n+1):
#     print(f"Enter the test data of device {i}")
#     device[f"device {i}"]=data()
# print("test data : ",device)




# test_info = {}
# while True:
#   test_check = input("Enter start or  exit: ")
#   if test_check == 'exit':
#       break
#   else:
#     test_check=='start'
#     device_id = input ( "Enter device id: " )
#     # if device_id.isnumeric() == False:
#     #     print ( "Invalid  format. Please enter again." )
#     #     continue
#     # else:
#     #     break
#     number=int(input("Enter no of  testing:"))
#     for i in range(1,number+1):
#     #        device_id = input ( "Enter device id: " )
#     #        if device_id.isnumeric() == False:
#     #            print ( "Invalid  format. Please enter again." )
#     #        else:
#     #            break
#        while True:
#            test_time= input( "Enter test time in the format of (HH:MM): " )
#            if len( test_time ) != 5  or test_time[2] != ':':
#                print("Invalid date format. Please enter again.")
#                continue
#            hour, time= test_time.split ( ':' )
#            if not (hour.isdigit () and time.isdigit ()):
#                  print ( "Invalid date format. Please enter again." )
#            else:
#                break
#        while True:
#            x_cordinate = input ( "Enter x cordinate: " )
#            if type( x_cordinate ) == False:
#                print ( "Invalid  format. Please enter again." )
#            else:
#                break
#        while True:
#            y_cordinate = float( input ( "Enter ty cordinate: " ) )
#            if type( y_cordinate ) == False:
#                print ( "Invalid  format. Please enter again." )
#            else:
#                break
#        while True:
#            test_number = input ( "Enter the test number: " )
#            if test_number.isnumeric() == False:
#                print ( "Invalid  format. Please enter again." )
#            else:
#                break
#        while True:
#            upper_limit = float( input ( "Enter the upper limit: " ) )
#            if type( upper_limit ) == False:
#                print ( "Invalid  format. Please enter again." )
#            else:
#                break
#        while True:
#            lower_limit =  input ( "Enter the lower limit: " )
#            if lower_limit.isnumeric () == False:
#                print ( "Invalid  format. Please enter again." )
#            else:
#                break
#        while True:
#            unit = input ( "Enter the unit: " )
#            if unit.isalpha() == False:
#                print ( "Invalid  format. Please enter again." )
#            else:
#                break
#
#
#        test_info[test_number] = {
#            'test name':x_cordinate,
#            'upper limit': y_cordinate,
#            'lower limit': lower_limit,
#            'unit': lower_limit,
#            'device id':device_id,
#            'test time':test_time,
#            'x cordinate':x_cordinate,
#            'y_cordinate':y_cordinate
#        }
#
# print("Device test information:",test_info)




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
    print(f"Enter the test data of device {i}")
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









