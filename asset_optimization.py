import csv
import numpy as np
import pandas
import statistics
import matplotlib.pyplot as plt
import seaborn as sn


def bootstrapping(data):
    my_samples = []
    negatives = 0

    for i in range(5000):
        x = np.random.choice(data[:-1], size=12, replace=True)

        my_samples.append(x.mean())

        if x.mean() < 0:
            negatives += 1

    proportion_neg = negatives/5000

    return statistics.mean(my_samples), proportion_neg


def asset_return(assets, data):
    flat_rate = 1/len(assets)
    individual_return = []
    negative_prop = []
    package_return = 0

    for i in assets:
        bootstrap_result = bootstrapping(data[i])
        package_return += flat_rate*bootstrap_result[0]
        individual_return.append(bootstrap_result[0])
        negative_prop.append(bootstrap_result[1])

    return package_return, individual_return, negative_prop


def correlation_matrix(data):
    corr_matrix = data.corr()
    sn.set(font_scale=0.8)
    sn.heatmap(corr_matrix, annot=True)
    plt.show()


def main():
    data = pandas.read_csv('data_w_cpi.csv')
    row_data = []
    assets = ['US LT (20Y) Corporate Bonds (TR)', 'US LT (20Y) Government Bonds (TR)',
              'US Intermediate-term (5Y) Government Bonds (TR)', 'US (30-Day) Treasury Bills',
              'AUSTRALIA Standard (Large+Mid Cap)', 'EUROPE Standard (Large+Mid Cap)',
              'GERMANY Standard (Large+Mid Cap)', 'HONG KONG Standard (Large+Mid Cap)',
              'JAPAN Standard (Large+Mid Cap)', 'UNITED KINGDOM Standard (Large+Mid Cap)',
              'Gold Return', 'CANADA Standard (Large+Mid Cap)', 'US Large-Cap Stocks (TR)',
              'US Small-Cap Stocks (TR)']

    #correlation_matrix(data)

    results = asset_return(assets, data)

    print(results[0])

    n = 0

    with open("negative_prop.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
        headers = ["Asset", "Asset Return", "Negative Proportion"]
        writer.writerow(headers)
        for i in assets:
            row_data = []
            row_data.append(i)
            row_data.append(results[1][n])
            row_data.append(results[2][n])
            writer.writerow(row_data)

            n += 1
    #bootstrapping(data[assets[1]], True)


main()

