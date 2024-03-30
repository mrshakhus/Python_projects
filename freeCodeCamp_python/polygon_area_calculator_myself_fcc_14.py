class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        rectangle = '*' * self.width + '\n'
        rectangle = rectangle * self.height
        return rectangle
    
    def get_amount_inside(self, some_rectangle):
        fit_in_widths = self.width//some_rectangle.width
        fit_in_heights = self.height//some_rectangle.height
        return fit_in_widths * fit_in_heights

class Square(Rectangle):
    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length
    
    def __repr__(self):
        return f'Square(side={self.width})'

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

Rectangle(3, 6)
Square(5)
Rectangle(3, 6).get_area()
Square(5).get_area()
Rectangle(3, 6).get_perimeter()
Square(5).get_perimeter()
Rectangle(3, 6).get_diagonal()
Square(5).get_diagonal()
Rectangle(15,10).get_amount_inside(Square(5))
Rectangle(4,8).get_amount_inside(Rectangle(3, 6))
Rectangle(2,3).get_amount_inside(Rectangle(3, 6))