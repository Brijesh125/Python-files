#1
"""
def binary_search(my_list,target):
    start = 0
    stop = len(my_list) - 1
    while start <= stop:
        mid = (start + stop) // 2
        if target == my_list[mid]:
            print("index of target : ", end="")
            return mid
        elif target < my_list[mid]:
            stop = mid - 1
        else:
            start = mid + 1

    if stop < 0:
        print("index of closest number : ",end="")
        return 0
    elif start >= len(my_list):
        print("index of closest number : ", end="")
        return len(my_list) - 1
    elif abs(target - my_list[start]) < abs(target - my_list[stop]):
        print("index of closest number : ", end="")
        return start
    else:
        print("index of closest number : ", end="")
        return stop

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    elements = int(input(f"Enter the index {i} element : "))
    my_list.append(elements)
my_list.sort()
print(my_list)
target = int(input("Enter the target : "))

print(binary_search(my_list,target))
"""
#2
"""
def ascii(string):
    dic={}
    for i in range(256):
        s=chr(i)
        for j in string:
            if s==j:
                dic[s]=i
    return dic

string=input("Enter the string : ")
print(ascii(string))
"""
#3
"""
def bit_pattern(*decimals):
    remainder_list = []
    for i in range(1,len(decimals)+1):
        decimal=decimals[-i]
        while decimal != 0:
            remainder = decimal % 2
            remainder_list.append(remainder)
            decimal = decimal // 2
        if len(remainder_list) > 8*i:
            return "Error"
        while len(remainder_list) < 8*i:
            remainder_list.append(0)
    reverse = remainder_list[::-1]
    print("data frame = ",end=" ")
    return reverse

print(bit_pattern(2,8,255))
"""
"""
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
"""
#4
"""
def decimal(list1):
    list2=[]
    list3=[]
    for i in range(0,len(list1),8):
        list2.append(list1[i:i+8])
    for i in list2:
        sum=0
        for j in range(len(i)):
            sum=sum+i[-j-1]*2**j
        list3.append(sum)
    tuple1=tuple(list3)
    print("tuple1 : ",end=" ")
    return tuple1
list1=[1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1]
print(decimal(list1))
"""
#5
"""
def combinestrings(*string):
    s=""
    for i in range(len(string)):
        if i==0:
            s=s+string[i]
        else:
            s=s+","+string[i]
    return '"'+s+'"'

print(combinestrings("GUUYG","UYGTF","GTTFY","DRED","EDTD"))
"""
#6
"""
def combinestrings(separator,*string):
    s=""
    for i in range(len(string)):
        if i==0:
            s=s+string[i]
        else:
            s=s+separator+string[i]
    return '"'+s+'"'

separator=input("Enter the separator string : ")
print(combinestrings(separator,"GUUYG","UYGTF","GTTFY","DRED","EDTD"))
"""
#7
"""
def KeyValueExists(Dict,**key_value):
    count=0
    for i in key_value.items():
        if i in Dict.items():
            count+=1
        if count==len(key_value):
            return True
    else:
        return False

Dict={'a':'1','b':'2','c':'3','z':'26'}
print(KeyValueExists(Dict,a='1',b='2',z='26'))
"""
#8
"""
def mean(my_list):
    sum=0
    for i in my_list:
        sum = sum + i
    mean = sum / len(my_list)
    return mean


def median(my_list):
    my_list.sort()
    l=len(my_list)
    if l % 2 == 0:
        return (my_list[l // 2] + my_list[(l // 2) - 1])/2
    else:
        return my_list[l // 2]


def mode(my_list):
    dict_mode = {}
    m=[]
    for i in my_list:
        count = my_list.count(i)
        dict_mode[i] = count
    for i, j in dict_mode.items():
        if max(dict_mode.values()) <= 1:
            return my_list
        else:
            if j == max(dict_mode.values()):
                m.append(i)
    return m


def fun(my_list,select):
    if select=="median":
        print(select, "=", end=" ")
        return median(my_list)
    elif select=="mode":
        print(select, "=", end=" ")
        return mode(my_list)
    else:
        print("mean =", end=" ")
        return mean(my_list)

select=input("Enter the mean,median or mode : ")
print(fun([2,3,4,6],select))
"""
"""
def main():
    slave = input("Enter the slave address : ")
    register = input("Enter the register address : ")
    data = input("Enter the data : ")
    num = [slave, register, data]
    serial_interface = []
    acknowledgement = responder(num)
    if type(acknowledgement) == str:
        print(acknowledgement)
    else:
        print("acknowledgement received : ", acknowledgement)
        if acknowledgement == [1, 1, 1]:
            for i in num:
                serial_interface = serial_interface + validate(i)
            print("serial interface : ", serial_interface)
        else:
            for i in range(len(acknowledgement)):
                if acknowledgement[i] == 0:
                    print(validate(num[i]))


def validate(decimal):
    try:
        decimal = int(decimal)
        temp = decimal
        remainder_list = []
        while (decimal != 0):
            remainder = decimal % 2
            remainder_list.append(remainder)
            decimal = decimal // 2
        while len(remainder_list) < 8:
            remainder_list.append(0)
        reverse = remainder_list[::-1]
        1 / (8 // len(reverse))
        return reverse
    except:
        return f"Error : binary of {temp} is greater than 8 bits"


def responder(num):
    respond = []
    for i in num:
        if i.isnumeric():
            if type(validate(i)) == str:
                respond.append(0)
            else:
                respond.append(1)
        else:
            return "Error : Invalid Decimal number entry"
    return respond


main()
"""
"""
def main():
    slave = input("Enter the slave address : ")
    register = input("Enter the register address : ")
    data = input("Enter the data : ")
    num = [slave, register, data]
    serial_interface = []
    acknowledgement = []
    for i in num:
        ack = responder(i)
        if type(ack) == str:
            return ack
        else:
            acknowledgement.append(ack)
    if len(acknowledgement) == len(num):
        print("acknowledgement received : ", acknowledgement)
    if acknowledgement == [1, 1, 1]:
        for i in num:
            serial_interface = serial_interface + validate(i)
        print("serial interface bits : ", end="")
        for i in serial_interface:
            print(i, end="")
        print("\n", "serial interface : ", end="")
        return serial_interface
    else:
        error_num = []
        for i in range(len(acknowledgement)):
            if acknowledgement[i] == 0:
                error_num.append(int(num[i]))
                error = validate(num[i]) + f"binary of {error_num} greater than 8 bits"
        return error


def validate(decimal):
    try:
        decimal = int(decimal)
        remainder_list = []
        while (decimal != 0):
            remainder = decimal % 2
            remainder_list.append(remainder)
            decimal = decimal // 2
        while len(remainder_list) < 8:
            remainder_list.append(0)
        reverse = remainder_list[::-1]
        1 / (8 // len(reverse))
        return reverse
    except:
        return "Error : "


def responder(num):
    if num.isnumeric() == False:
        return "Error : Invalid Decimal number entry"
    else:
        if type(validate(num)) == str:
            return 0
        else:
            return 1

print(main())
"""