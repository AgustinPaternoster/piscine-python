Exercice 02: my first decorating
Turn-in directory : ex02/
Files to turn in : callLimit.py
Allowed functions : None

Write a function that takes as argument a call limit of another function and blocks
its execution above a limit.

The prototype of functions is:
def callLimit(limit: int):
count = 0
def callLimiter(function):
def limit_function(*args: Any, **kwds: Any):
#your code here

Your tester.py:
from callLimit import callLimit
@callLimit(3)
def f():
print ("f()")
@callLimit(1)
def g():
print ("g()")
for i in range(3):
f()
g()

Expected output:
$> python tester.py
f()
g()
f()
Error: <function g at 0x7fabdc243ee0> call too many times
f()
Error: <function g at 0x7fabdc243ee0> call too many times
$>