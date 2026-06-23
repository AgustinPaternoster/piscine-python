"""Displays life expectancy projections for a given country."""

from load_csv import load
import matplotlib.pyplot as plt

country = 'Spain'


def main():
    df = load("life_expectancy_years.csv")
    spain_serie = df.set_index('country').loc[country]
    spain_serie.plot()
    plt.title('Spain Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.show()


if __name__ == "__main__":
    main()
