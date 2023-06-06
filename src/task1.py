import matplotlib.pyplot as plt
import distributions as distr


def draw_distr(distr_type):
    bins_num = 25
    sample_size = [10, 50, 1000]
    plt_name = distr_type + '_distribution'
    plt.figure(figsize=(15, 5)).suptitle(plt_name)
    for size in range(len(sample_size)):
        sample = distr.sample(distr_type, sample_size[size])
        plt.subplot(1, 3, size + 1)
        n, bins, patches = plt.hist(sample, bins_num, density=True, edgecolor='black', alpha=0.6)
        y = distr.density_func(distr_type, bins)
        plt.plot(bins, y, color='red', lw=1)
        plt.title('N=%i' % sample_size[size], fontsize=10)
        plt.xlabel('numbers')
        plt.ylabel('density')
    # plt.show()
    plt.savefig("C:/Учеба/LaTeX/4 семестр/MathStat_report_1-4/" + plt_name + ".png")


def lab1_run():
    for distribution in distr.distributions:
        draw_distr(distribution)
