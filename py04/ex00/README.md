Exercice 00: Calculate my statistics
Turn-in directory : ex00/
Files to turn in : statistics.py
Allowed functions : None
You must take in *args a quantity of unknown number and make the Mean, Median,
Quartile (25% and 75%), Standard Deviation and Variance according to the **kwargs
ask.
You have to manage the errors.

The prototype of function is:
def ft_statistics(*args: Any, **kwargs: Any) -> None:
#your code here

Your tester.py:
from statistics import ft_statistics
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")

Expected output:
$> python tester.py
mean : 95.6
median : 42
quartile : [11.0, 64.0]
-----
std : 17982.70124086944
var : 323377543.9183673
-----
-----
ERROR
ERROR
ERROR
$>