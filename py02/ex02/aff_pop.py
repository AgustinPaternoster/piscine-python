from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import sys

def plot_format(x, pos):
    if x >= 1000000000:
        return f'{x/1000000000:.1f}B'
    elif x >= 1000000:
        return f'{x/1000000:.0f}M'
    elif x >= 1000:
        return f'{x/1000:.0f}k'
    else:
        return f'{x:.0f}'


def df_format(valor):
    multipliers = {'m': 1000000 , 'k': 1000, 'b':1000000000}
    if valor.isdecimal() or pd.isna(valor):
        return int(valor)
    return int((float(valor[:-1]) * multipliers[valor[-1].lower()]))

def main():
    try:
        df = load("population_total.csv")
        if df is None:
            return
        country_1 = sys.argv[1].capitalize()
        country_2 = sys.argv[2].capitalize()
        
        if country_1 not in df['country'].values or country_2 not in df['country'].values:
            raise ValueError('countries not found in the file')
        df_filtered = df.set_index('country').loc[[country_1, country_2], :'2050']
        country_1_serie = df_filtered.iloc[0].apply(df_format)
        country_2_serie = df_filtered.iloc[1].apply(df_format)
        fig, ax = plt.subplots()
        ax.plot(country_1_serie, color='blue', label=country_1)
        ax.plot(country_2_serie, color='red', label=country_2)
        plt.legend()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
        ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=4))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(plot_format))
        plt.show()       
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()
