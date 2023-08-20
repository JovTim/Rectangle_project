def rectangle_area(length: int, width: int) -> int:
    ''''
Calculate the area of the rectangle using the length and width.

Args:
    length - The length of the rectangle
    width - The height of the rectangle

Return
    The calculated area of the rectangle
'''
    return length * width

def rectangle_perimeter(length: int, width: int) -> int:
    """
Calculate the perimeter of the rectangle using length and width

Args:
    length - The length of the rectangle
    width - The width of the rectangle

Return:
    The  calculated perimeter of the rectangle
"""
    return 2 * (length + width)

user_length = int(input("Enter length of Rectangle: "))
user_width = int(input("Enter width of Rectangle: "))

print(f'The Area of the Rectangle: {rectangle_area(user_length, user_width)}')
print(f'The Perimeter of the Rectangle: {rectangle_perimeter(user_length, user_width)}')