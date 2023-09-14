#Amstrong
num=int(input("Enter the number : "))
tem=num
sum=0
while(tem!=0):
    rem=tem%10
    cube=rem**3
    sum=sum+cube
    tem=tem//10
if sum==num:
    print(num,"is an Amstrong number")
else:
    print(num,"is not an Amstrong number")