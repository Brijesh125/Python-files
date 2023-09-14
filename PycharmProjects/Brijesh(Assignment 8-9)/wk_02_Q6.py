separator=input("Enter the separator string : ")
n=int(input("Enter the number of strings : "))
string=""
for i in range(1,n+1):
    ip_string=input(f"Enter the string {i} : ")
    if i==1:
        string=string+ip_string
    else:
        string=string+separator+ip_string
print("output :",string)