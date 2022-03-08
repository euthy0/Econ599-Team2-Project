import csv
import numpy as np
import pandas
import statistics
import matplotlib.pyplot as plt
import seaborn as sn


def bootstrapping(data, visual):
    my_samples = []
    for i in range(5000):
        x = np.random.choice(data, size=12, replace=True)
        my_samples.append(x.mean())

    if visual is True:
        plt.hist(my_samples)

    return statistics.median(my_samples)


def asset_return(assets, data):
    flat_rate = 1/len(assets)
    package_return = 0
    for i in assets:
        package_return += flat_rate*bootstrapping(data[i])

    return package_return


def correlation_matrix(data):
    corr_matrix = data.corr()
    sn.set(font_scale=0.8)
    sn.heatmap(corr_matrix, annot=True)
    plt.show()


def main():
    data = pandas.read_csv('data_w_cpi.csv')

    assets = ['US LT (20Y) Corporate Bonds (TR)', 'US LT (20Y) Government Bonds (TR)',
              'US Intermediate-term (5Y) Government Bonds (TR)', 'US (30-Day) Treasury Bills',
              'AUSTRALIA Standard (Large+Mid Cap)', 'EUROPE Standard (Large+Mid Cap)',
              'GERMANY Standard (Large+Mid Cap)', 'HONG KONG Standard (Large+Mid Cap)',
              'JAPAN Standard (Large+Mid Cap)', 'UNITED KINGDOM Standard (Large+Mid Cap)',
              'Gold Return', 'CANADA Standard (Large+Mid Cap)', 'US Large-Cap Stocks (TR)',
              'US Small-Cap Stocks (TR)']

    correlation_matrix(data)
    #results = asset_return(assets, data)
    #print(results)
    #bootstrapping(data[assets[1]], True)


main()

