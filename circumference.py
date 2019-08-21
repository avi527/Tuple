#write a programm using a function that return the area and circumference
#of a circle whose radius is passed as an argument.

PI=3.14
def cal_a_r(r):
    return (PI*r*r)
radius=float(input("Enter the radius : "))
(area,circumference)=cal_a_r(radius)
print("Area of the circle with radius",radius,"= ",area)
print("circumference of the circle with radius ", radius,"=",circumference)
