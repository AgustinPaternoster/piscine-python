class calculator:
    """Calculator class for vector-scalar operations."""

    def __init__(self, vec):
        """Initialize calculator with a vector.

        Args:
            vec: List of integers or floats.

        Raises:
            ValueError: If vector is empty or contains invalid types.
        """
        if len(vec) < 1:
            raise ValueError("Vector can't be empty")
        if not all([isinstance(x, (int,float)) for x in vec]):
            raise ValueError("Invalid data type")
        self.vector = vec

    def __add__(self, object)->None:
        """Add scalar to each element of the vector."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self,object)-> None:
        """Multiply each element of the vector by scalar."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object)-> None:
        """Subtract scalar from each element of the vector."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self,object)-> None:
        """Divide each element of the vector by scalar.

        Raises:
            ValueError: If scalar is 0.
        """
        if object == 0:
            raise ValueError("Division by 0")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
