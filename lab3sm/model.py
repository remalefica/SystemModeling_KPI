from termcolor import colored
import numpy as np
from copy import deepcopy

from elements.process import Process
from elements.create import Create
from elements.dispose import Dispose


def dict_concat(dictionary):
    result_dictionary = {}
    for d in dictionary:
        for k, v in d.items():
            result_dictionary[str(k)] = v
    return result_dictionary


def dict_concat_in_lists(dictionary):
    result_dictionary = {}
    for d in dictionary:
        for k, v in d.items():
            result_dictionary.setdefault(k, []).append(v)
    return result_dictionary


class Model:
    def __init__(self, elements: list):
        self.list = elements
        self.event = 0
        self.t_next = 0.0
        self.t_curr = self.t_next
        self.device_load = list()

    # здійснення імітації на інтервалі часу time
    def simulate(self, time, flag=True):
        while self.t_curr < time:
            # встановити t_next на max value of float
            self.t_next = float('inf')
            self.choose_event()
            # показати кроки
            if flag:
                print('\nIt\'s time for event in {0}, time = {1}'.format(
                    colored(self.list[self.event].get_name(), 'cyan'), str(self.t_next)))

            for e in self.list:
                e.calculate(self.t_next - self.t_curr)

            #просунутися у часі вперед
            self.t_curr = self.t_next
            # оновити поточний час для кожного елементу
            for e in self.list:
                e.t_curr = self.t_curr

            self.finish()

            # показати кроки
            if flag:
                self.print_info()
        return self.result()

    def finish(self):
        self.list[self.event].out_act()
        for e in self.list:
            if self.t_curr in e.t_next:
                e.out_act()

    def choose_event(self):
        for e in self.list:
            t_next_val = np.min(e.t_next)
            if t_next_val < self.t_next:  # знаходимо найменший з моментів часу
                self.t_next = t_next_val
                self.event = e.id_el

    def print_info(self):
        for e in self.list:
            e.print_info()

    def result(self):
        global_quantity = 0
        global_dispose = 0
        global_max_load = 0
        global_mean_queue = 0
        global_max_observed_queue = 0
        global_failure_probability = 0
        global_mean_load = 0
        process_statistics_list = list()
        num_processors = 0

        print('\n-------------RESULTS-------------')
        for e in self.list:
            if isinstance(e, Create):
                c = deepcopy(e)
                global_quantity = c.result(self.t_curr)
                del c

            if isinstance(e, Dispose):
                d = deepcopy(e)
                global_dispose += d.result(self.t_curr)
                del d

            if isinstance(e, Process):
                p = deepcopy(e)
                num_processors += 1

                process_id = p.id_el
                process_stat = p.result(self.t_curr, process_id)
                process_statistics_list.append(process_stat)

                if p.quantity == 0:
                    failure_probability = 0
                else:
                    failure_probability = p.failure / (p.failure + float(p.quantity))

                max_queue = p.max_observed_queue
                mean_queue = process_stat['MeanQueue' + str(process_id)]
                mean_load = process_stat['MeanLoad' + str(process_id)]

                if mean_load > global_max_load:
                    global_max_load = mean_load

                if max_queue > global_max_observed_queue:
                    global_max_observed_queue = max_queue

                global_mean_queue += mean_queue
                global_failure_probability += failure_probability
                global_mean_load += mean_load

                print(
                    'average observed value of queue = {0}'
                    '\nmaximum observed value of queue = {1}'
                    '\naverage observed value of device loading = {2}'
                    '\nfailure = {3}'
                    '\nfailure probability = {4}'.format(str(mean_queue), str(max_queue), str(mean_load),
                                                         str(p.failure), str(failure_probability)))

                del process_id, process_stat, p, mean_load, mean_queue, max_queue, failure_probability

        pro = dict_concat(process_statistics_list)
        del e, process_statistics_list

        global_mean_queue /= num_processors
        global_failure_probability /= num_processors
        global_mean_load /= num_processors

        print(colored('\nCALCULATING GLOBAL VALUES', 'magenta'))
        print('dispose quantity = {0}\nglobal average observed value of queue = {1}'
              '\nglobal maximum observed value of queue = {2}'
              '\nglobal average observed value of device loading = {3}'
              '\nglobal maximum observed value of device loading = {4}'
              '\nglobal failure probability = {5}\n'.format(str(global_dispose), str(global_mean_queue),
                                                            str(global_max_observed_queue), str(global_mean_load),
                                                            str(global_max_load), str(global_failure_probability)))

        return {
                   'CreateQuantity': global_quantity,
                   'DisposeQuantity': global_dispose,
                   'G.MeanQueue': global_mean_queue,
                   'G.MaxQueue': global_max_observed_queue,
                   'F.p.': global_failure_probability,
                   'G.MeanLoad': global_mean_load,
                   'G.MaxLoad': global_max_load
               }, pro
