from universal_algorithm.model import Model
from universal_algorithm.elements.process import Process
from universal_algorithm.elements.create import Create
from termcolor import colored


class BankModel(Model):
    def __init__(self, elements: list):
        super().__init__(elements)
        self.num_clients = 0
        self.num_iterations = 0
        self.allowed_transfers = None
        self.transfers = None
        self.transfer_condition = 1
        self.time_in_bank = dict()

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

            if isinstance(self.list[self.event], Create):
                self.time_in_bank[self.list[self.event].quantity] = [self.t_curr, self.finish()]
            elif isinstance(self.list[self.event], Process):
                self.finish()

            self.try_change_queue()
            self.calculate_num_clients()
            # показати кроки
            if flag:
                self.print_info()
        return self.result()

    def finish(self):
        t_pr = self.list[self.event].out_act()
        for e in self.list:
            if self.t_curr in e.t_next:
                e.out_act()
        return t_pr

    def calculate_num_clients(self):
        self.num_iterations += 1
        for e in self.list:
            if isinstance(e, Process):
                # зайняті
                for s in range(len(e.states)):
                    if e.states[s] == 1:
                        self.num_clients += 1
                self.num_clients += e.queue

    def try_change_queue(self):
        queue_sizes_list = list()

        if self.allowed_transfers is not None:
            # for first iteration
            if self.transfers is None:
                for e in self.allowed_transfers:
                    # transferring is allowed only between Processes
                    if isinstance(e, Process):
                        queue_sizes_list.append(e.queue)
                    else:
                        self.allowed_transfers.remove(e)
                self.transfers = [0] * len(queue_sizes_list)
            else:
                for e in self.allowed_transfers:
                    queue_sizes_list.append(e.queue)

            for i in range(len(queue_sizes_list)):
                for j in range(len(queue_sizes_list)):
                    if i != j:
                        if queue_sizes_list[i] - queue_sizes_list[j] >= self.transfer_condition:
                            self.list[self.allowed_transfers[i].id_el].queue -= 1
                            self.list[self.allowed_transfers[j].id_el].queue += 1
                            print(colored('TRANSFER: From ' + self.allowed_transfers[i].name + '\'s queue to ' +
                                          self.allowed_transfers[j].name + '\'s queue', 'red'))
                            self.transfers[i] += 1

    def print_process(self, e, mean_queue, max_queue, mean_load, failure_probability):
        super().print_process(e, mean_queue, max_queue, mean_load, failure_probability)
        print('avg time interval between departures from windows = {0}'.format(str(e.quantity/self.t_curr)))
        if e in self.allowed_transfers:
            print('transfers (from) = {0}'.format(str(self.transfers[self.allowed_transfers.index(e)])))

    def result_global(self):
        self.calculate_global_values()
        self.print_global_values('\nBANK STATISTICS')

    def print_global_values(self, header):
        super().print_global_values(header)
        print('avg number of clients in bank = {0}'.format(str(self.num_clients/self.num_iterations)))

