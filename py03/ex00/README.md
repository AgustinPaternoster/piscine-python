Chapter III
Exercise 00
Exercise 00
Exercice 00: GOT S1E9
Turn-in directory : ex00/
Files to turn in : S1E9.py
Allowed functions : None

Create an abstract class "character" which can take a first_name as first parameter,
is_alive as second non mandatory parameter set to True by default and can change the
health state of the character with a method that passes is_alive from True to False.
And a "stark" class which inherits from Character

The prototype of Class is:
from abc import ABC, abstractmethod
class Character(ABC):
"""Your docstring for Class"""
@abstractmethod
#your code here
class Stark(Character):
"""Your docstring for Class"""
#your code here

Your tester.py:

from S1E9 import Character, Stark
Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)
4Training Piscine Python for datascience - 3
Oriented Object Programming
Expected output: (docstrings can be different)

$> python tester.py
{'first_name': 'Ned', 'is_alive': True}
True
False
Your docstring for Class
Your docstring for Constructor
Your docstring for Method
---
{'first_name': 'Lyanna', 'is_alive': False}
$>

Make sure you have used an abstract class, the code below should make
an error.
from S1E9 import Character

hodor = Character("hodor")
TypeError: Can't instantiate abstract class Character with abstract method
$>