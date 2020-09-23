import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from termcolor import cprint

from hi_squared_table import find_table_hi_squared


def print_name(num):
    cprint('\n\t___GENERATOR #' + str(num) + '___', 'cyan', attrs=['bold'])


def print_extra_info(average, dispersion, observed_chi_2, expected_chi_2, result):
    print('\naverage: ' + str(average))
    print('dispersion: ' + str(dispersion))
    print('X squared (observed): ' + str(observed_chi_2))
    print('X squared (expected): ' + str(expected_chi_2))
    print('The found distribution law corresponds to the observed values of the random variable: ' + str(result))


def get_average_and_dispersion(array):
    s = 0
    average = array.sum() / array.size

    for i in array:
        s += pow(i - average, 2)

    dispersion = s / (array.size - 1)
    return average, dispersion


def get_intervals(array, num_of_intervals):
    interval_size = (array.max() - array.min()) / num_of_intervals  # 20 - number of intervals

    entries_list = list()
    limit_1 = array.min()

    for i in range(0, num_of_intervals):
        limit_2 = limit_1 + interval_size

        counter = 0
        for n in array:
            if limit_1 <= n < limit_2:
                counter += 1

        entries_list.append([[limit_1, limit_2], counter])
        limit_1 = limit_2

    return entries_list


def pull_intervals_from_list(entries, num_of_intervals):
    interval_list = list()
    for i in range(num_of_intervals):
        interval_list.append([entries[i][0][0], entries[i][0][1]])
    return interval_list


def to_data_frame(arr, num_of_intervals):
    copy_arr = [x[:] for x in arr]
    for i in range(num_of_intervals):
        name_interval = str(round(copy_arr[i][0][0], 2)) + '-' + str(round(copy_arr[i][0][1], 2))
        copy_arr[i][0] = name_interval

    df = pd.DataFrame(copy_arr, columns=['Intervals', 'Values'])
    return df


def plot_histogram(entries_list, num_of_intervals):
    df_e = to_data_frame(entries_list, num_of_intervals)

    print(df_e.head(num_of_intervals))

    sns.barplot(data=df_e, x='Intervals', y='Values')
    plt.xticks(rotation=-45)
    plt.show()


def get_chi_squared(expected_list, observed_list, num_of_intervals):
    chi_2 = 0
    for i in range(num_of_intervals):
        expected = 10000 * expected_list[i]
        chi_2 += pow(observed_list[i] - expected, 2) / expected
    return chi_2


def chi_2_tool(expected_list, observed_list, num_of_intervals):
    observed_chi_squared = get_chi_squared(expected_list, observed_list, num_of_intervals)
    expected_chi_squared = find_table_hi_squared(num_of_intervals - 1)
    return observed_chi_squared, expected_chi_squared
