# Created by: Viviana Hurtado
# Date: may 24 2025
# This programs calculates the area amd perimeter of a rectangle with the information given by the user
# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Formulas to calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Display the results
print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")
