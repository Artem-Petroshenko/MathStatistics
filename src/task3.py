import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
import distributions as ds
import os
import seaborn as sns
import pandas as pd


def draw_boxplot(distr_type, sample_size):
    plt_name = 'boxplot_' + distr_type
    data_dict = {}
    fig, ax = plt.subplots()
    for size in sample_size:
        key = "n =" + str(size)
        data_dict[key] = ds.sample(distr_type, size)
    df = pd.DataFrame(dict([(key, pd.Series(value)) for key, value in data_dict.items()]))
    sns.boxplot(data=df, orient="h", ax=ax).set_title(distr_type)
    plt.savefig("C:/Учеба/LaTeX/4 семестр/MathStat_report_1-4/" + plt_name + ".png")


def find_min_boarder(sample):
    return np.quantile(sample, 0.25) - 1.5 * (np.quantile(sample, 0.75) - np.quantile(sample, 0.25))


def find_max_boarder(sample):
    return np.quantile(sample, 0.25) + 1.5 * (np.quantile(sample, 0.75) - np.quantile(sample, 0.25))


def count_emissions(sample, min_border, max_border):
    total = 0
    for el in sample:
        if el < min_border or el > max_border:
            total += 1
    return total


def emissions_share(sample_size, repeats):
    rows = []
    for distr in ds.distributions:
        for size in sample_size:
            share = 0
            for _ in range(repeats):
                sample = ds.sample(distr, size)
                min_border = find_min_boarder(sample)
                max_border = find_max_boarder(sample)
                share += count_emissions(sample, min_border, max_border)
            share /= repeats
            rows.append(distr + " n = $" + str(size) + "$ & $" + str(np.around(share / size, decimals=3)) + "$")
    with open("share_of_emission.tex", "w") as f:
        f.write("\\begin{tabular}{|c|c|}\n")
        f.write("\\hline\n")
        f.write("Sample & Share of emissions \\\\\n")
        f.write("\\hline\n")
        for row in rows:
            f.write(row + "\\\\\n")
            f.write("\\hline\n")
        f.write("\\end{tabular}")


def lab3_run():
    sample_size = [20, 100]
    repeats = 1000
    emissions_share(sample_size, repeats)
    # for distr in ds.distributions:
    #     draw_boxplot(distr, sample_size)

