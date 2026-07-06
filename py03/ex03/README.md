Exercice 03: Calculate my vector
Turn-in directory : ex03/
Files to turn in : ft_calculator.py
Allowed functions : None
Write a calculator class that is able to do calculations (addition, multiplication, sub-
traction, division) of vector with a scalar.

The prototype of Class is:
class calculator:
#your code here
def __add__(self, object) -> None:
#your code here
def __mul__(self, object) -> None:
#your code here
def __sub__(self, object) -> None:
#your code here
def __truediv__(self, object) -> None:
#your code here

Your tester.py:
from ft_calculator import calculator
v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
Print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
Print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5

Expected output: (docstrings can be different)
$> python tester.py
[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
---
[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
---
[5.0, 10.0, 15.0]
[1.0, 2.0, 3.0]
$>
You don’t have to do any error handling, except for the division by 0