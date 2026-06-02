from tqdm import tqdm
from time import sleep
import os

def ft_tqdm(lst: range)-> None:
    
    terminalSize = os.get_terminal_size().columns
    total = len(lst)
    counterWidth = int(len(str(total)))
    completed = 0
    barSize = terminalSize - ((counterWidth * 2) + 2) - 4 - 4 - 25
    for x in lst:
        completed  += 1
        percentage = int((completed / total) * 100)
        barCompletion = int((barSize/total) * completed)
        barEmpty = barSize - barCompletion
        if completed == total:
            barString = "=" * barCompletion
        elif completed > 0:
            barString = ("=" * (barCompletion - 1)) + ">"
        print(f'{percentage:3}%', end='') # porcentaje
        print(f'|[{barString}{" " * barEmpty}]|', end=" ") # barra
        print(f'{completed:{counterWidth}}/{total}', end='')
        print('\r', end='') # final
        yield
    print()
    pass


