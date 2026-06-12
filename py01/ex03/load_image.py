from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path:str) -> np.ndarray:
    try:
        with Image.open(path) as img:
            vector = np.array(img)
        print(f'The shape of the image is: {vector.shape}')
        return vector
    except FileNotFoundError as e:
        print(f'Error: The file {path} was not found')
    except UnidentifiedImageError as e:
        print(f'Error: The file {path} is not a valid imagen')
    except Exception as e:
        print(f'Error: {e}')