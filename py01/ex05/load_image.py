
from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the specified path, prints its shape,
    and returns its pixel values as a NumPy array.

    Args:
        path (str): The path to the image file.

    Returns:
        np.ndarray: Pixel values of the image, or None on error.
    """
    try:
        with Image.open(path) as img:
            img_rgb = img.convert('RGB')
            vector = np.array(img_rgb)
        print(f'The shape of the image is: {vector.shape}')
        return vector
    except FileNotFoundError:
        print(f'Error: The file {path} was not found')
    except UnidentifiedImageError:
        print(f'Error: The file {path} is not a valid imagen')
    except Exception as e:
        print(f'Error: {e}')
