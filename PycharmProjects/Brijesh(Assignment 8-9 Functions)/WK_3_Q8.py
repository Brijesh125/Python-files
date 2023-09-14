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


def fun(my_list,select="mean"):
    if select=="mean":
        print(select,"=",end=" ")
        return mean(my_list)
    elif select=="median":
        print(select, "=", end=" ")
        return median(my_list)
    elif select=="mode":
        print(select, "=", end=" ")
        return mode(my_list)
    else:
         return "invalid"


print(fun([2,3,4,6],"mode"))