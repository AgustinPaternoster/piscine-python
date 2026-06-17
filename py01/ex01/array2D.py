"""
Module for 2D array operations.
"""
import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D array (list of lists) from start to end indices.

    Prints the original shape and the new shape of the sliced list.

    Args:
        family (list): A 2D list.
        start (int): The starting index for the slice.
        end (int): The ending index for the slice.

    Returns:
        list: The sliced 2D list.
    """
    if not isinstance(family, list):
        raise ValueError("Family must be a list")
    if len(family) < 1:
        raise ValueError("family can't be an empty list")
    if not all(len(i) == len(family[0]) for i in family):
        raise ValueError("Family can't  be a Jagged Lists")
    vec = np.array(family)
    print(f'My shape is: {vec.shape}')
    newVec = vec[start:end]
    print(f'My new shape is: {newVec.shape}')
    return newVec.tolist()
