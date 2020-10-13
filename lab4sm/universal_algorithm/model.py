from termcolor import colored
import numpy as np
from copy import deepcopy

from universal_algorithm.elements.process import Process
from universal_algorithm.elements.create import Create
from universal_algorithm.elements.dispose import Dispose
from universal_algorithm.dict_concat import dict_concat


class Model:
    def __init__(self, elements: list):
        self.list = elements
        self.event = 0
        self.t_next = 0.0
        self.t_curr = self.t_next
        self.device_load = list()
        self.global_dispose = 0
        self.global_max_load, self.global_mean_load = 0, 0
        self.global_mean_queue, self.global_max_observed_queue = 0, 0
        self.global_failure_probability = 0
        self.num_processors = 0

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

            # просунутися у часі вперед
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
        print('\n-------------RESULTS-------------')
        for e in self.list:
            if isinstance(e, Create):
                c = deepcopy(e)
                c.result(self.t_curr)
                del c

            if isinstance(e, Dispose):
                d = deepcopy(e)
                self.global_dispose += d.result(self.t_curr)
                del d

            if isinstance(e, Process):
                self.num_processors += 1
                self.result_process(e)

        del e
        self.result_global()

    def result_process(self, e):
        mean_queue, max_queue, mean_load, failure_probability = self.calculate_process(e)
        self.print_process(e, mean_queue, max_queue, mean_load, failure_probability)

    def calculate_process(self, e):
        p = deepcopy(e)
        process_id = p.id_el
        # get dict of p(quantity, mean_queue, mean_load, fails
        process_stat = p.result(self.t_curr, process_id)

        failure_probability = 0 if p.quantity == 0 else p.failure / (p.failure + float(p.quantity))

        max_queue = p.max_observed_queue
        mean_queue = process_stat['MeanQueue' + str(process_id)]
        mean_load = process_stat['MeanLoad' + str(process_id)]

        if mean_load > self.global_max_load:
            self.global_max_load = mean_load

        if max_queue > self.global_max_observed_queue:
            self.global_max_observed_queue = max_queue

        self.global_mean_queue += mean_queue
        self.global_failure_probability += failure_probability
        self.global_mean_load += mean_load

        del process_id, process_stat, p
        return mean_queue, max_queue, mean_load, failure_probability

    def print_process(self, e, mean_queue, max_queue, mean_load, failure_probability):
        print(
            'avg queue = {0}'
            '\nmax queue = {1}'
            '\navg loading = {2}'
            '\nfailures = {3}'
            '\nfailure probability = {4}'.format(str(mean_queue), str(max_queue), str(mean_load),
                                                 str(e.failure), str(failure_probability)))
        del mean_load, mean_queue, max_queue, failure_probability

    def result_global(self):
        self.calculate_global_values()
        self.print_global_values('\nCALCULATING GLOBAL VALUES')

    def calculate_global_values(self):
        self.global_mean_queue /= self.num_processors
        self.global_failure_probability /= self.num_processors
        self.global_mean_load /= self.num_processors

    def print_global_values(self, header):
        print(colored(header, 'magenta'))
        print('dispose quantity = {0}\nglobal avg queue = {1}'
              '\nglobal max queue = {2}'
              '\nglobal avg loading = {3}'
              '\nglobal max loading = {4}'
              '\nglobal failure probability = {5}'.format(str(self.global_dispose), str(self.global_mean_queue),
                                                          str(self.global_max_observed_queue),
                                                          str(self.global_mean_load), str(self.global_max_load),
                                                          str(self.global_failure_probability)))
