import random_generator as rg

class Model:
    # waiting_time_list - список для обчислення середнього часу очікування черзі
    # delta_T_list - список для обчислення середнього завантаження пристрою
    # queue_length_list - список довжин черг в момент t_curr
    def __init__(self, delay_create, delay_process, max_q=None):
        self.t_next = 0.0               # момент часу наступної події
        self.t_curr = self.t_next       # поточний момент часу
        self.t0 = self.t_curr           # момент часу наступної моделі надходження
        self.t1 = float('inf')
        self.delay_create = float(delay_create)     # затримка надходження
        self.delay_process = float(delay_process)   # затримка обслуговування
        self.num_create, self.num_process, self.failure = 0, 0, 0
        self.max_queue = 0 if max_q is None else max_q      # обмеження на чергу
        self.queue, self.state, self.next_event = 0, 0, 0   # стан пристрою, стан черги, наступна подія
        self.waiting_time_list, self.delta_T_list, self.queue_length_list = list(), list(), list()

    def simulate(self, time_modeling, flag):
        while self.t_curr < time_modeling:
            self.t_next = self.t0
            self.next_event = 0  # надходження заявки

            if self.t1 < self.t_next:
                self.t_next = self.t1
                self.next_event = 1

            self.waiting_time_list.append((self.t_next - self.t_curr) * self.queue)
            self.delta_T_list.append((self.t_next - self.t_curr) * self.state)

            self.t_curr = self.t_next
            self.event0() if self.next_event == 0 else self.event1()

            if flag:
                self.print_info()
            self.queue_length_list.append(self.state)

        if flag:
            print('\n\t___VERIFICATION___')
        self.print_statistics()

    def event0(self):
        self.t0 = self.t_curr + self.get_delay_of_create()
        self.num_create += 1
        if self.state == 0:
            self.state = 1
            self.t1 = self.t_curr + self.get_delay_of_process()
        else:
            if self.queue < self.max_queue:
                self.queue += 1
            else:
                self.failure += 1

    def event1(self):
        self.t1 = float('inf')
        self.state = 0
        if self.queue > 0:
            self.queue -= 1
            self.state = 1
            self.t1 = self.t_curr + self.get_delay_of_process()
        self.num_process += 1

    def print_info(self):
        print('t = ' + str(self.t_curr) + ' state = ' + str(self.state) + ' queue = ' + str(self.queue))

    def print_statistics(self):
        print('delayCreate = ' + str(round(self.delay_create, 2)) +
              '; delayProcess = ' + str(round(self.delay_process, 2)) +
              '; maxQueue = ' + str(round(self.max_queue, 2)) +
              '; numCreate = ' + str(self.num_create) +
              '; numProcess = ' + str(self.num_process) +
              '; failure = ' + str(self.failure) +
              '; Qavg = ' + str(round(self.get_sum_waiting_time() / self.num_process, 6)) +     # сер. час очікування
              '; Ravg = ' + str(round(self.get_sum_delta_t() / self.t_next, 6)) +               # завантаження пристрою
              '; Lavg = ' + str(round(self.get_sum_waiting_time() / self.t_next, 6)) +          # сер. довжина черги
              '; probability = ' + str(round(self.get_probability_of_failure(), 6)))            # ймовірність відмови

    def get_delay_of_create(self):
        return rg.exp(self.delay_create)

    def get_delay_of_process(self):
        return rg.exp(self.delay_process)

    def get_probability_of_failure(self):
        return float(self.failure / self.num_create)

    def get_sum_waiting_time(self):
        return sum(self.waiting_time_list)

    def get_sum_delta_t(self):
        return sum(self.delta_T_list)