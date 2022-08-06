
from Shapes import *
def saad():
    input1 =str(input("Write the name of the shape you want to try on :"))
    if input1 == "Square":
        Square.Display()
        num = int(input("\nEnter 1 to calculate the area or enter 2 to calculate the Perimeter :"))
        if num == 1:
          Square.Calculate_Area()
        elif num == 2:
         Square.Calculate_Perimeter()
    elif input1 == "Rectangle":
        Rectangle.Display()
        num = int(input("\nEnter 1 to calculate the area or enter 2 to calculate the Perimeter :"))
        if num == 1:
            area_rec = Rectangle.Calculate_area()
            print(area_rec)
        elif num == 2:
            Rectangle.Calculate_perimeter()
    elif input1 == "Triangle":
        Triangle.Display()
        num = int(input("\nEnter 1 to calculate the area or enter 2 to calculate the Perimeter :"))
        if num == 1:
         Triangle.calculate_area()
        elif num == 2:
            Triangle.calculate_perimeter()
    else:
        print("Try agin")

saad()
wors = str(input("Do you want to restart the program to work in another form? \nSelect your answer with yes or no :"))
while wors == "yes":
    saad()
