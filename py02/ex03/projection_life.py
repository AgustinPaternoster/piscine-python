import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load

def plot_format(x, pos):
    if x >= 1000000000:
        return f'{x/1000000000:.1f}B'
    elif x >= 1000000:
        return f'{x/1000000:.0f}M'
    elif x >= 1000:
        return f'{x/1000:.0f}k'
    else:
        return f'{x:.0f}'

def render_plot(df: pd.Dataframe):
    fig , ax = plt.subplots()
    ax.set_xlim(290,11000)
    ax.set_xscale('log')
    valores = [300, 1000, 10000]
    ax.set_xticks(valores)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(plot_format))
    ax.scatter(df['1900_gdp'], df['1900_years'], s=40)
    plt.show()
    


def main():
    try:
        gdp = load('./income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
        if gdp is None:
            return
        life= load('../life_expectancy_years.csv')
        if life is None:
            return
        df_merge = pd.merge(gdp[['country', '1900']], life[['country','1900']], on="country", suffixes=("_gdp", "_years"))
        df_clean = df_merge.dropna()
        render_plot(df_clean)
    except Exception as e:
        print(f'Error: {e}') 
    return

if __name__ == "__main__":
    main()