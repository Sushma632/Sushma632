class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Yield the length and width in the required format
        yield {'length': self.length}
        yield {'width': self.width}

# Function to get user input and create a Rectangle instance
def create_rectangle_from_input():
    try:
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        
        rectangle = Rectangle(length, width)

        return rectangle
    except ValueError:
        print("Please enter valid integer values for length and width.")
        return None

# Example usage
rectangle = create_rectangle_from_input()
if rectangle:
    for dimension in rectangle:
        print(dimension)
