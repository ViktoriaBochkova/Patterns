class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width ** 2

    def calculate_perimeter(self):
        return 4 * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Triangle(Shape):
    def __init__(self, width, a, b):
        self.a = a
        self.b = b
        self.width = width

    def calculate_area(self):
        return (self.a * self.width) / 2

    def calculate_perimeter(self):
        return self.a + self.b + self.width


class ShapeFactory:
    def create_shape(self, name):
        if name == 'Круг':
            radius = input("Введите радиус вашей фигуры: ")
            return Circle(float(radius))
        elif name == 'Прямоугольник':
            height = input("Введите высоту вашей фигуры: ")
            width = input("Введите ширину вашей фигуры: ")
            return Rectangle(int(height), int(width))
        elif name == 'Квадрат':
            width = input("Введите ширину вашей фигуры: ")
            return Square(int(width))
        elif name == 'Треугольник':
            width = input("Введите ширину вашей фигуры: ")
            a = input("Введите сторону A вашей фигуры: ")
            b = input("Введите сторону B фигуры: ")
            return Triangle(int(width), int(a), int(b))


shape_factory = ShapeFactory()
shape_name = input("Введите тип фигуры: ")

shape = shape_factory.create_shape(shape_name)

print(f"Расчет параметров для фигуры: {shape_name}")
print(f"Площадь {shape_name}а : {shape.calculate_area()}")
print(f"Периметр {shape_name}а : {shape.calculate_perimeter()}")
