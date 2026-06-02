from tqdm import tqdm
from time import sleep
import os

def ft_tqdm(lst: range)-> None:
    
    terminalSize = os.get_terminal_size().columns
    arr = [ n + 1 for n in lst]
    total = arr[-1]
    counterWidth = int(len(str(total)))
    completed = 0
    barSize = terminalSize - ((counterWidth * 2) + 2) - 4 - 4 - 25
    for i in arr:
        percentage = int((i / total) * 100)
        completed  += 1
        barCompletion = int((barSize/total) * i)
        barEmpty = barSize - barCompletion
        print(f'{percentage:3}%', end='') # porcentaje
        print(f'|[{"=" * barCompletion}{" " * barEmpty}]|', end=" ") # barra
        print(f'{completed:{counterWidth}}/{total}', end='')
        print('\r', end='') # final
        yield
    print()
    pass


