"""
This module provides functions to apply color filters (invert, red, green,
blue, grey) to a NumPy array image and display them using matplotlib.
"""
import os

if (os.environ.get('XDG_SESSION_TYPE') == 'wayland'
        and 'QT_QPA_PLATFORM' not in os.environ):
    os.environ['QT_QPA_PLATFORM'] = 'wayland'

import numpy as np
import matplotlib.pyplot as plt


def ft_invert(image: np.array) -> np.array:
    """
    Inverts the color channels of the image.
    """
    try:
        invert_img = image.copy()
        if len(image.shape) == 3 and image.shape[2] == 4:
            invert_img[:, :, :3] = 255 - image[:, :, :3]
        else:
            invert_img = 255 - image
        print(invert_img)

        plt.imshow(invert_img)
        plt.title("image Inverted")
        plt.show()
        return invert_img
    except Exception as e:
        print(f'Error: {e}')


def ft_red(image: np.array) -> np.array:
    """
    Applies a red filter to the image, keeping only the red channel.
    """
    red_img = image.copy()
    try:
        red_img[:, :, 2] = red_img[:, :, 2] * 0
        red_img[:, :, 1] = red_img[:, :, 1] * 0
        print(red_img)
        plt.imshow(red_img)
        plt.title("image red")
        plt.show()
        return red_img
    except Exception as e:
        print(f'Error: {e}')


def ft_green(image: np.array) -> np.array:
    """
    Applies a green filter to the image, keeping only the green channel.
    """
    green_img = image.copy()
    try:
        green_img[:, :, 0] = green_img[:, :, 0] - green_img[:, :, 0]
        green_img[:, :, 2] = green_img[:, :, 2] - green_img[:, :, 2]
        print(green_img)
        plt.imshow(green_img)
        plt.title("image green")
        plt.show()
        return green_img
    except Exception as e:
        print(f'Error: {e}')


def ft_blue(image: np.array) -> np.array:
    """
    Applies a blue filter to the image, keeping only the blue channel.
    """
    blue_img = image.copy()
    try:
        blue_img[:, :, 0] = 0
        blue_img[:, :, 1] = 0
        print(blue_img)
        plt.imshow(blue_img)
        plt.title("image blue")
        plt.show()
        return blue_img
    except Exception as e:
        print(f'Error: {e}')


def ft_grey(image: np.array) -> np.array:
    """
    Converts the image to grayscale
    preserving the alpha channel if present.
    """
    try:
        grey_img = image.copy()
        grey_channel = np.sum(grey_img[:, :, :3], axis=2) / 3
        grey_img[:, :, 0] = grey_channel
        grey_img[:, :, 1] = grey_channel
        grey_img[:, :, 2] = grey_channel
        print(grey_img)
        plt.imshow(grey_img)
        plt.title("image grey")
        plt.show()
        return grey_img
    except Exception as e:
        print(f'Error: {e}')
