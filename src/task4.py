import numpy as np
import distributions as ds
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from statsmodels.distributions.empirical_distribution import ECDF


def empiric():
    sizes = [20, 60, 100]
    for distr in ds.distributions:
        if distr == "Poisson":
            interval = np.arange(6, 14, 1)
        else:
            interval = np.arange(-4, 4, 0.01)
        fig, ax = plt.subplots(1, 3, figsize=(12, 4))
        plt.subplots_adjust(wspace=0.5)
        fig.suptitle(distr)
        for j in range(len(sizes)):
            arr = ds.sample(distr, sizes[j])
            for a in arr:
                if distr == "Poisson" and (a < 6 or a > 14):
                    arr = np.delete(arr, list(arr).index(a))
                elif distr != "Poisson" and (a < -4 or a > 4):
                    arr = np.delete(arr, list(arr).index(a))

            ax[j].set_title("n = " + str(sizes[j]))
            if distr == "Poisson":
                ax[j].step(interval, [ds.distr_func(distr, x) for x in interval], color='#DDA0DD')
            else:
                ax[j].plot(interval, [ds.distr_func(distr, x) for x in interval], color='#DDA0DD')
            if distr == "Poisson":
                arr_ex = np.linspace(6, 14)
            else:
                arr_ex = np.linspace(-4, 4)
            ecdf = ECDF(arr)
            y = ecdf(arr_ex)
            ax[j].step(arr_ex, y, color='blue', linewidth=0.5)
        plt.savefig("C:/Учеба/LaTeX/4 семестр/MathStat_report_1-4/" + distr + "_emperic.png")


def kernel():
    sizes = [20, 60, 100]
    for distr in ds.distributions:
        if distr == "Poisson":
            interval = np.arange(6, 15, 1)
        else:
            interval = np.arange(-4, 4, 0.01)
        for j in range(len(sizes)):
            arr = ds.sample(distr, sizes[j])
            for a in arr:
                if distr == "Poisson" and (a < 6 or a > 14):
                    arr = np.delete(arr, list(arr).index(a))
                elif distr != "Poisson" and (a < -4 or a > 4):
                    arr = np.delete(arr, list(arr).index(a))

            title = ["h = 1/2 * h_n", "h = h_n", "h = 2 * h_n"]
            bw = [0.5, 1, 2]
            fig, ax = plt.subplots(1, 3, figsize=(12, 4))
            plt.subplots_adjust(wspace=0.5)
            for k in range(len(bw)):
                kde = gaussian_kde(arr, bw_method='silverman')
                h_n = kde.factor
                fig.suptitle(distr + ", n = " + str(sizes[j]))
                ax[k].plot(interval, ds.density_func(distr, interval), color='blue', alpha=0.5, label='density')
                ax[k].set_title(title[k])
                sns.kdeplot(arr, ax=ax[k], bw=h_n * bw[k], label='kde', color='black')
                ax[k].set_xlabel('x')
                ax[k].set_ylabel('f(x)')
                ax[k].set_ylim([0, 1])
                if distr == 'Poisson':
                    ax[k].set_xlim([6, 14])
                else:
                    ax[k].set_xlim([-4, 4])
                ax[k].legend()
            plt.savefig("C:/Учеба/LaTeX/4 семестр/MathStat_report_1-4/" + distr + "_kernel_n" + str(sizes[j]) + ".png")


def lab4_run():
    empiric()
    kernel()
