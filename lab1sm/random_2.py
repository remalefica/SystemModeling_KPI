import random
import numpy as np

import utility as util
import functions as fn


def get_myu():
    myu = 0
    for i in range(0, 12):
        myu += random.random()
    return myu - 6


class Random2:
    def __init__(self, alpha, sigma, num_of_values):
        self.alpha = alpha
        self.sigma = sigma
        self.num_of_values = num_of_values

    def create_array(self):
        x_array = np.array([])
        for i in range(0, self.num_of_values):
            myu = get_myu()
            x_array = np.append(x_array, self.sigma * myu + self.alpha)
        return x_array

    def get_expected_values(self, dispersion, entries, num_of_intervals):
        expected_list = list()
        interval_list = util.pull_intervals_from_list(entries, num_of_intervals)

        for i in range(num_of_intervals):
            expected_list.append(self.calculate_normal(dispersion, interval_list, i))
        return expected_list

    def calculate_normal(self, dispersion, interval_list, i):
        x = (interval_list[i][1] + interval_list[i][0]) / 2
        num = fn.dis_fun(self.alpha, dispersion, x)
        if num > 0.5:
            return 1 - num
        else:
            return num

    def analyze(self, num_of_intervals):
        util.print_name(2)

        array = self.create_array()
        average, dispersion = util.get_average_and_dispersion(array)

        entries = util.get_intervals(array, num_of_intervals)
        util.plot_histogram(entries, num_of_intervals)

        observed_list = [i[1] for i in entries]

        expected_list = self.get_expected_values(dispersion, entries, num_of_intervals)

        observed_chi_squared, expected_chi_squared = util.chi_2_tool(expected_list, observed_list, num_of_intervals)

        util.print_extra_info(average, dispersion, observed_chi_squared, expected_chi_squared,
                              observed_chi_squared < expected_chi_squared)


