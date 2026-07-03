
Exercice 02: Now it’s weird!
Turn-in directory : ex02/
Files to turn in : Files from previous exercises + DiamondTrap.py
Allowed functions : None

In this exercise, you will create a monster: Joffrey Baratheon.
This is so risky!
There is something inconsistent with this new "false" king.
You must use the Properties to change the physical characteristics of our new king.
The prototype of Class is:
from S1E7 import Baratheon, Lannister
class King(Baratheon, Lannister):
#your code here

Your tester.py:
from DiamondTrap import King
Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

Expected output: (docstrings can be different)
$> python tester.py
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hair': 'dark'}
blue
light
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'blue', 'hairs': 'light'}
$>

Since python 2.3 the language uses C3 linearization to counter the
problem of inheritance in diamand.