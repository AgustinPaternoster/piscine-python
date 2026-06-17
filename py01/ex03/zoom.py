import sys
import os

if (os.environ.get('XDG_SESSION_TYPE') == 'wayland'
        and 'QT_QPA_PLATFORM' not in os.environ):
    os.environ['QT_QPA_PLATFORM'] = 'wayland'

from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    Main function to load animal.jpeg, slice it to a 400x400 zoomed section,
    convert it to a single color channel (grayscale), and display it.
    """
    try:
        img = ft_load("animal.jpeg")
        if img is None:
            return
        print(img)
        img = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])
        h, w = img.shape
        zh, zw = 400, 400
        x = round((h - zh) / 2)
        y = round((w - zw) / 2)
        zimg = img[x:(x + zh), y:(y + zw)].astype(np.uint8)
        print(f'New shape after slicing: ({zw}, {zh})')
        print(zimg)

        plt.imshow(zimg, cmap='gray')
        plt.title("Zoomed Grayscale")
        plt.show()
        # problema con el entorno grafico , revisar en el equipo 42.
    except KeyboardInterrupt:
        print("\nExecution interrupted by the user.")
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
