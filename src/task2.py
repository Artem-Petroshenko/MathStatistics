import distributions as distr
import numpy as np
from math import *


def median(sample, size):
    if len(sample) % 2:
        return sample[size // 2]
    else:
        return (sample[size // 2 - 1] + sample[size // 2]) / 2


def z_r(sample, size):
    return (sample[0] + sample[size - 1]) / 2


def quart(sample, size, p):
    k = size * p
    if k.is_integer():
        return sample[int(k)]
    else:
        return sample[int(k) + 1]


def z_q(sample, size):
    return (quart(sample, size, 0.25) + quart(sample, size, 0.75)) / 2


def z_tr(sample, size):
    r = int(size / 4)
    res = 0
    for i in range(r + 1, size - r + 1):
        res += sample[i]
    return res / (size - 2 * r)


def lab2_run():
    sample_size = [10, 100, 1000]
    repeats = 1000

    with open("C:/Учеба/LaTeX/4 семестр/MathStat_report_1-4.tex", "a") as f:
        for distribution in distr.distributions:
            f.write("\\textbf{" + distribution + "} \\\\\n")
            for size in sample_size:
                f.write("    \\underline{Размер выборки " + str(size) + " элементов} \\\\\n")
                s_mean, s_median, s_z_r, s_z_q, s_z_tr = [], [], [], [], []
                for _ in range(repeats):
                    sample = distr.sample(distribution, size)
                    s_mean.append(np.mean(sample))
                    s_median.append(median(sample, size))
                    s_z_r.append(z_r(sample, size))
                    s_z_q.append(z_q(sample, size))
                    s_z_tr.append(z_tr(sample, size))

                E_mean = np.around(np.mean(s_mean), decimals=4)
                E_median = np.around(np.mean(s_median), decimals=4)
                E_z_r = np.around(np.mean(s_z_r), decimals=4)
                E_z_q = np.around(np.mean(s_z_q), decimals=4)
                E_z_tr = np.around(np.mean(s_z_tr), decimals=4)

                D_mean = np.around(np.mean(np.multiply(s_mean, s_mean)) - E_mean ** 2, decimals=4)
                D_median = np.around(np.mean(np.multiply(s_median, s_median)) - E_median ** 2, decimals=4)
                D_z_r = np.around(np.mean(np.multiply(s_z_r, s_z_r)) - E_z_r ** 2, decimals=4)
                D_z_q = np.around(np.mean(np.multiply(s_z_q, s_z_q)) - E_z_q ** 2, decimals=4)
                D_z_tr = np.around(np.mean(np.multiply(s_z_tr, s_z_tr)) - E_z_tr ** 2, decimals=4)

                f.write("    \\begin{tabular}{|c|c|c|c|c|c|}\n")
                f.write("    \\hline\n")
                f.write("    & $\\overline{x}$ & median & $z_r$ & $z_Q$ & $z_tr$ \\\\\n")
                f.write("    \\hline\n")
                f.write("    $E(z)$ & " + f"{E_mean} & "
                                          f"{E_median} & "
                                          f"{E_z_r} & "
                                          f"{E_z_q} & "
                                          f"{E_z_tr} \\\\\n")
                f.write("    \\hline\n")
                f.write("    $D(z)$ & " + f"{D_mean} & "
                                          f"{D_median} & "
                                          f"{D_z_r} & "
                                          f"{D_z_q} & "
                                          f"{D_z_tr} \\\\\n")
                f.write("    \\hline\n")

                mean_left, mean_right = np.around(E_mean - sqrt(D_mean), decimals=4), np.around(E_mean + sqrt(D_mean),
                                                                                                decimals=4)
                median_left, median_right = np.around(E_median - sqrt(D_median), decimals=4), \
                                            np.around(E_median + sqrt(D_median), decimals=4)
                z_r_left, z_r_right = np.around(E_z_r - sqrt(D_z_r), decimals=4), np.around(E_z_r + sqrt(D_z_r),
                                                                                            decimals=4)
                z_q_left, z_q_right = np.around(E_z_q - sqrt(D_z_q), decimals=4), np.around(E_z_q + sqrt(D_z_q),
                                                                                            decimals=4)
                z_tr_left, z_tr_right = np.around(E_z_tr - sqrt(D_z_tr), decimals=4), np.around(E_z_tr + sqrt(D_z_tr),
                                                                                                decimals=4)

                f.write("    $E(x) - \\sqrt(D(z))$ & " + f"{mean_left} & "
                                                        f"{median_left} & "
                                                        f"{z_r_left} & "
                                                        f"{z_q_left} & "
                                                        f"{z_tr_left} \\\\\n")

                f.write("    \\hline\n")
                f.write("    $E(x) + \\sqrt(D(z))$ & " + f"{mean_right} & "
                                                         f"{median_right} & "
                                                         f"{z_r_right} & "
                                                         f"{z_q_right} & "
                                                         f"{z_tr_right} \\\\\n")
                f.write("    \\hline\n")

                mean_point = round((mean_left + mean_right) / 2)
                mediana_point = round((median_left + median_right) / 2)
                z_r_point = round((z_r_left + z_r_right) / 2)
                z_q_point = round((z_q_left + z_q_right) / 2)
                z_tr_point = round((z_tr_left + z_tr_right) / 2)

                f.write("    $\\hat{E}$ & " + f"{mean_point} & "
                                              f"{mediana_point} & "
                                              f"{z_r_point} & "
                                              f"{z_q_point} & "
                                              f"{z_tr_point} \\\\\n")

                f.write("    \\hline\n")
                f.write("    \\end{tabular}")
