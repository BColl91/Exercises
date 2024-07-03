import math

def calculateArea(width, height):
    """Calculate the area of a rectangle."""
    return width * height

def circleArea(diameter):
    """Calculate the area of a circle."""
    radius = diameter / 2
    return math.pi * radius * radius

# Get the width and height from the user for the rectangle
width = float(input("Enter the width of a rectangle in cms: "))
height = float(input("Enter the height of the same rectangle in cms: "))

print(""" """)

# Calculate the area of the rectangle
rectangle_area = calculateArea(width, height)
print("The area of the rectangle is: {:.2f} sq. cms".format(rectangle_area))

print(""" """)

# Get the diameter from the user for the circle
diameter = float(input("Enter the diameter of a circle in cms: "))

print(""" """)

# Calculate the area of the circle
circle_area = circleArea(diameter)
print("The area of the circle is: {:.2f} sq. cms".format(circle_area))
