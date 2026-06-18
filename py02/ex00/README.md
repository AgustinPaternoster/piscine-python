Exercise 00
Exercise 00
Exercice 00: Load my Dataset
Turn-in directory : ex00/
Files to turn in : load_csv.py
Allowed functions : pandas or any lib for data set manipulation
Make a function that takes a path as argument, writes the dimensions of the data set
and returns it. You have to handle the error cases and return None if the path is bad,
bad format...
def load(path: str) -> Dataset: (You have to adapt the type of return according to your library)
#your code here
Your script tester:
from load_csv import load
print(load("life_expectancy_years.csv"))
$> python tester.py
Loading dataset of dimensions (195, 302)
country 1800 1801 1802 1803 ... 2096 2097 2098 2099 2100
Afghanistan 28.2 28.2 28.2 28.2 ... 76.2 76.4 76.5 76.6 76.8
...
$>
You can display the Dataset in any format you like, the given format
is not restrictive.