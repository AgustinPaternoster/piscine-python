import numpy as  np

lista = [[[1,1,1],[2,2,2]],
         [[3,3,3],[4,4,4]]]

img = [[[120, 45, 200],[89, 210, 34]],
        [[15, 230, 89], [112, 45, 167]]
    ]


img_inverted = [
        # Fila 0
        [
            [135, 210, 55],  # Píxel (0,0) - [255-120, 255-45, 255-200]
            [166, 45, 221]   # Píxel (0,1) - [255-89, 255-210, 255-34]
        ],
        # Fila 1
        [
            [240, 25, 166],  # Píxel (1,0) - [255-15, 255-230, 255-89]
            [143, 210, 88]   # Píxel (1,1) - [255-112, 255-45, 255-167]
        ]
    ]



# invert
tmp = np.array(img) - 255

redFilter = [1,0,0]

# filtro red
tmpRed = np.array(img) * np.array(redFilter)
print(tmpRed)

# filtro red
tmpgreen = 
print("no")