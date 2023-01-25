#Calculate the area of a circle and assign the value to _area_of_circle_
radius=30
pi=3.14
_area_of_circle_=pi*pow(radius,2)
print("area of the circle with radius 30 :",_area_of_circle_)

#Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
_circum_of_circle_=2*pi*radius
print("circumference of the circle is with radius 30 :",_circum_of_circle_)

#Radius as input and calculate the area.
r=input('Enter the radius:')
r=int(r)
area=pi*pow(r,2)
print("area of the circle is :",area)
