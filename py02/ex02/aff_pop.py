from load_csv import load
import matplotlib.pyplot as plt

country_1 = 'Spain'
country_2 = 'France'

def main():
    df = load("population_total.csv")
    spain_serie = df.set_index('country').loc[country_1]
    # spain_serie.plot()
    # plt.title('Spain Life expectancy Projections')
    # plt.xlabel('Year')
    # plt.ylabel('Life expectancy')
    # plt.show()
    print(spain_serie)

if __name__ == "__main__":
    main()
