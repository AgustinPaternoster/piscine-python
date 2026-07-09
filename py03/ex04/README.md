Exercice 04: Calculate my dot product
Turn-in directory : ex04/
Files to turn in : ft_calculator.py
Allowed functions : None
Write a calculator class that is able to do calculations (dot product, addition, sub-
traction) of 2 vectors.
Vector will always have identical sizes, no error handling.
It’s up to you to find a decorator that can help you to use the Methods of the calculator
class without instantiating this class.

The prototype of Class is:
class calculator:
#your code here
# decorator
def dotproduct(V1: list[float], V2: list[float]) -> None:
#your code here
# decorator
def add_vec(V1: list[float], V2: list[float]) -> None:
#your code here
# decorator
def sous_vec(V1: list[float], V2: list[float]) -> None:
#your code here
Your tester.py:

from ft_calculator import calculator
a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)

Expected output: (docstrings can be different)
$> python tester.py
Dot product is: 56
Add Vector is : [7.0, 14.0, 5.0]
Sous Vector is: [3.0, 6.0, -1.0]
$>
You don’t have to do any error handling