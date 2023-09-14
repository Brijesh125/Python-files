#pseudocode
'''
step 1:take the coordinates as user input
step 2:create 2 tuples with the coordinates
step 3:apply the difference between coordinates ((x2-x1) as x and (y2-y1) as y )to distance eqn (x^2+y^2)^.5
      use index for getting coordinates from tuple
step 4:print both tuples and distance
'''

x1=int(input("Enter the x1 coordinate : "))
y1=int(input("Enter the y1 coordinate : "))
x2=int(input("Enter the x2 coordinate : "))
y2=int(input("Enter the y2 coordinate : "))
tuple_1=(x1,y1)
tuple_2=(x2,y2)
distance=((tuple_2[0]-tuple_1[0])**2+(tuple_2[1]-tuple_1[1])**2)**.5
print("tuple 1 : ",tuple_1)
print("tuple 2 : ",tuple_2)
print("distance = ",distance)

