class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, n):
        self.width = n

    def set_height(self, n):
        self.height = n

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        string = ''
        for n in range(self.height):
            string += '*' * self.width + '\n'
        return string

    def get_amount_inside(self, instance):
        width = self.width // instance.width
        height = self.height // instance.height
        return width * height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, n):
        self.width = n
        self.height = n
