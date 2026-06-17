import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculates the BMI (Body Mass Index) for a list of heights and weights.

    Args:
        height (list): A list of integers or floats representing heights (in meters).
        weight (list): A list of integers or floats representing weights (in kg).

    Returns:
        list: A list of calculated BMI values.

    Raises:
        TypeError: If elements in height or weight lists are not integers or floats.
        ValueError: If size of height and weight lists do not match.
    """
    if not all(isinstance(c, (int, float)) for c in height):
        raise TypeError(
            "All elements in the lists must be positive integers or floats."
        )
    if not all(isinstance(c, (int, float)) for c in weight):
        raise TypeError(
            "All elements in the lists must be positive integers or floats."
        )
    if len(weight) != len(height):
        raise ValueError("height and weight lists must be of the same size.")
    height_array = np.array(height)
    weight_array = np.array(weight)
    result = weight_array / (height_array ** 2)
    return result.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if BMI values in a list exceed a specified limit threshold.

    Args:
        bmi (list): A list of BMI values (integers or floats).
        limit (int): The threshold limit.

    Returns:
        list: A list of booleans (True if BMI > limit, False otherwise).

    Raises:
        TypeError: If elements in bmi list are not integers or floats.
    """
    if not all(isinstance(c, (int, float)) for c in bmi):
        raise TypeError(
            "All elements in the lists must be positive integers or floats."
        )
    vector = np.array(bmi)
    mask = vector > limit
    return mask.tolist()

