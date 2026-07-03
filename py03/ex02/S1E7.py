from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""
    family_name = "Lannister"
    eyes = "blue"
    hairs = "light"

    def die(self):
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)

    def __str__(self):
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"    

