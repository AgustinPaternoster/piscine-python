import numpy as np

def slice_me(family:list , start: int , end: int)-> list:
    if not isinstance(family, list):
        raise ValueError("Family must be a list")
    if len(family) < 1:
        raise ValueError("family can't be an empty list")
    if not all( len(i) == len(family[0]) for i in family):
        raise ValueError("Family can't  be a Jagged Lists")
    vec = np.array(family)
    print(f'My shape is: {vec.shape}')
    newVec = vec[start:end]
    print(f'My new shape is: {newVec.shape}')
    return newVec.tolist()


