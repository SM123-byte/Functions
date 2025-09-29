# Finding Circumference of a Circle

 # Creating a function for method of circumference

def circle_work_out(radius):
    circumference = radius * 3.14 * 2
    return circumference

 # Using user input for radius

radius = float(input("Enter the radius of the circle: "))

 # Calling function and printing circumference

circle_circumference = circle_work_out(radius)
print(f"The circumference of the circle is {circle_circumference}")