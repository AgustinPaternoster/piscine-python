Exercice 01: Outer_inner
Turn-in directory : ex01/
Files to turn in : in_out.py
Allowed functions : None

Write a function that returns the square of argument, a function that returns the
Exponentiation of argument by himself and a function that takes as argument a number
and a function, it returns an object that when called returns the result of the arguments
calculation.

The prototype of functions is:
def square(x: int | float) -> int | float:
#your code here
def pow(x: int | float) -> int | float:
#your code here
def outer(x: int | float, function) -> object:
count = 0
def inner() -> float:
#your code here

Your tester.py:
from in_out import outer
from in_out import square
from in_out import pow
my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())

Expected output:
$> python tester.py
9
81
6561
---
1.8371173070873836
3.056683336818703
30.42684786675409
$>
We remind you that the use of global is forbidden