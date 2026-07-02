from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character in a story."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Character with first name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Change the alive status of the character to False."""
        pass


class Stark(Character):
    """Concrete class representing a Stark character."""

    def die(self):
        """Change the alive status of the Stark to False."""
        self.is_alive = False
