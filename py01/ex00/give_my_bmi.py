import numpy as np


# bmi = kg/ (heght)2

def give_bmi(height: list[int | float], weight: list[int | float])-> list[int | float]:
    if not all(isinstance(c, int) or isinstance(c, float)for c in height):
        raise TypeError("All elements in the lists must be positive integers or floats.")
    if not all(isinstance(c, int) or isinstance(c, float) for c in weight):
        raise TypeError("All elements in the lists must be positive integers or floats.")
    if len (weight) != len(height):
        raise ValueError("height and weight lists must be of the same size.")
    height = np.array(height)
    weight = np.array(weight)
    result = weight / (height ** 2)
    return result.tolist()

def apply_limit(bmi: list[int|float], limit: int)->list[bool]:
    if not all(isinstance(c, int) or isinstance(c, float) for c in bmi):
        raise TypeError("All elements in the lists must be positive integers or floats.")
    vector = np.array(bmi)
    mask = vector > limit
    return mask.tolist()
