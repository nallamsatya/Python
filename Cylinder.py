PI = 3.14
radius = float(input('Please Enter the Radius of a Cylinder: '))
height = float(input('Please Enter the Height of a Cylinder: '))

surface = 2 * PI * radius * (radius + height)
Volume = PI * radius * radius * height

print("Surface area of a Cylinder will be %.2f" %surface)
print("Volume of a Cylinder will be %.2f" %Volume)
