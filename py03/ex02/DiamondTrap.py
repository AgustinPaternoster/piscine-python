from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """Representing King Joffrey, a Baratheon-Lannister hybrid."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a King with first name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = self.__class__.family_name
        self.eyes = self.__class__.eyes
        self.hairs = self.__class__.hairs

    def get_eyes(self):
        """Return the eye color of the King."""
        return self.eyes

    def set_eyes(self, color):
        """Set the eye color of the King."""
        self.eyes = color

    def get_hairs(self):
        """Return the hair color of the King."""
        return self.hairs

    def set_hairs(self, color):
        """Set the hair color of the King."""
        self.hairs = color


