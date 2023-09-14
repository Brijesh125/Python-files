def main():
    slave = input("Enter the slave address : ")
    register = input("Enter the register address : ")
    data = input("Enter the data : ")
    num = [slave, register, data]
    serial_interface=[]
    acknowledgement=responder(num)
    if type(acknowledgement)==str:
        return acknowledgement
    else:
        if acknowledgement == [1, 1, 1]:
            for i in num:
                serial_interface = serial_interface + validate(i)
            print("acknowledgement received : ",acknowledgement)
            print("serial interface : ",end="")
            return serial_interface
        else:
            index = acknowledgement.index(0)
            print("acknowledgement received : ", acknowledgement)
            return validate(num[index])

def validate(decimal):
    decimal=int(decimal)
    temp=decimal
    remainder_list = []
    while (decimal != 0):
        remainder = decimal % 2
        remainder_list.append(remainder)
        decimal = decimal // 2
    if len(remainder_list) > 8:
        return f"Error : binary of {temp} is greater than 8 bits"
    while len(remainder_list) < 8:
        remainder_list.append(0)
    reverse = remainder_list[::-1]
    return reverse

def responder(num):
    respond=[]
    for i in num:
        if i.isnumeric():
            if type(validate(i))==str:
                respond.append(0)
            else:
                respond.append(1)
        else:
            return "Error : Invalid Decimal number entry"
    return respond

print(main())

# def bit_pattern(*decimals):
#     remainder_list = []
#     for i in range(1,len(decimals)+1):
#         decimal=decimals[-i]
#         while decimal != 0:
#             remainder = decimal % 2
#             remainder_list.append(remainder)
#             decimal = decimal // 2
#         if len(remainder_list) > 8*i:
#             return "Error"
#         while len(remainder_list) < 8*i:
#             remainder_list.append(0)
#     reverse = remainder_list[::-1]
#     print("data frame = ",end=" ")
#     return reverse
#
# print(bit_pattern(2,8,255))