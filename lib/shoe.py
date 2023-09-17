# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        return f"The {self.brand} shoe has been repaired."
