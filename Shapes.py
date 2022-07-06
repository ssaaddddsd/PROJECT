
class shape:
    
    def __init__(self,Length : float , Width : float ):
        self.Length = Length
        self.Width = Width
     
class Square(shape): 
    def __init__(self,Length : float , Width : float ):
         super().__init__ (self, Length , Width )
    
    def Display():
        print("\nThis is mathematical laws related to the square :")
        print()
        print("Area of ​​the square = side length * side length")
        print("Perimeter of the square = 4 x side length")

    def Calculate_Area():
        input_length = float(input("Enter the length :"))
        print("Area is :",input_length*input_length)
    
    def Calculate_Perimeter():
       inputi = float(input("Enter the length : "))
       print("Perimeter is : ", inputi *4)
      
class Rectangle(shape):
    def __init__(self,Length : float , Width : float ):
         super().__init__ (self, Length , Width )

    def Display():
        print("\nThis is mathematical laws related to the Rectangle :")
        print()
        print("Area of the Rectangle = Length * Width")
        print("Perimeter of the Rectangle = (Length + Width) * 2  ")

    def Calculate_area():
        length = float (input("Enter the Length :"))
        width = float(input("Enter the width : "))
        area_rec = length * width
        return area_rec
       
    def Calculate_perimeter():
        length = float (input("Enter the Length :"))
        width = float(input("Enter the width : "))
        print("Perimeter of this rectangle : ", (length + width)*2)

class Triangle(shape):
    def __init__(self,base_Length : float , Height : float ):
        self.base_Length = base_Length
        self.Height = Height

    def Display():
        print("\nThis is mathematical laws related to the Triangle  :")
        print()
        print("Area of ​​a triangle = half the length of the base x the height , or (base length x height) ÷ 2")
        print("The perimeter of a triangle is equal to the sum of the lengths of its sides")
    
    def calculate_area():
        base_length = float(input("Enter the base length :"))
        height = float(input("Enter the height: "))
        print("The area of this triangle : ", (base_length*height) / 2)

    def calculate_perimeter():
        len1 =float(input("Enter The length of the first side :"))
        len2 = float(input("Enter the length of the second side : "))
        len3 = float(input("Enter the length of the third side :"))
        print("Perimeter of this triangle : " ,len1 + len2 + len3 )
