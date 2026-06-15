import sys
import os

if os.environ.get('XDG_SESSION_TYPE') == 'wayland' and 'QT_QPA_PLATFORM' not in os.environ:
    os.environ['QT_QPA_PLATFORM'] = 'wayland'

import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt
import sys

def main():
    try:
        img = ft_load('animal.jpeg')
        img = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])
        h, w = img.shape
        zh , zw = 400, 400
        x = round((h - zh) / 2)
        y = round((w - zw )/ 2)
        zimg = img[x:(x + zh),y:(y + zw)].astype(np.uint8)
        print(f'The shape of image is: ({zw}, {zh})')
        print(zimg)
        traspose_img = np.zeros((zh,zw))
        for h in range(zh):
            for w in range(zw):
                traspose_img[w][h] = zimg[h][w]
        print(f'New shape after Transpose: {traspose_img.shape}')
        print(traspose_img)


        plt.imshow(traspose_img, cmap='gray')
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
