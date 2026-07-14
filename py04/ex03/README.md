Exercice 03: data class
Turn-in directory : ex03/
Files to turn in : new_student.py
Allowed functions : dataclasses, random, string

Write a dataclass that takes as arguments a name and nickname, set active to True,
create the student login, and generate a random ID with the generate_id function.
You must not use __str__ , __repr__ in your class.

The prototype of function and class is:
import random
import string
from dataclasses import dataclass, field
def generate_id() -> str:
return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
#your code here
Your tester.py:
from new_student import Student
student = Student(name = "Edward", surname = "agle")
print(student)

Expected output: (id is random)
$> python tester.py
Student(name='Edward', surname='agle', active=True, login='Eagle', id='trannxhndgtolvh')
$>

The login and id should not be initializable and must return an
error.
Your tester.py:
from new_student import Student
student = Student(name = "Edward", surname = "agle", id = "toto")
print(student)
Expected output:
$> python tester.py
...
TypeError: Student.__init__() got an unexpected keyword argument 'id'
$>