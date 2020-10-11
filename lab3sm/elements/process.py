import numpy as np
import element as e


class Process(e.Element):
    def __init__(self, delay, channel=1):
        super().__init__(delay)
        self.name = 'PROCESSOR' + str(self.id_el)
        self.queue, self.max_observed_queue = 0, 0
        self.max_queue = float('inf')
        self.mean_queue = 0.0
        self.failure = 0
        self.channel = channel
        self.t_next = [float('inf')] * self.channel
        self.states = [0] * self.channel
        self.probability = [1]
        self.mean_load = 0

    def in_act(self):
        # region modified code
        free_devices = self.get_free_devices()
        for i in free_devices:
            self.states[i] = 1
            self.t_next[i] = self.t_curr + super().get_delay()  # set час звільнення пристрою
            break
        else:
            if self.queue < self.max_queue:
                self.queue += 1
            else:
                self.failure += 1
        # endregion

        # region initial code
        # if super().get_state() == 0:
        #     super().set_state(1)
        #     super().set_t_next(super().get_t_curr() + super().get_delay())
        # else:
        #     if self.queue < self.max_queue:
        #         self.queue = self.queue + 1
        #     else:
        #         self.failure += 1
        # endregion

    def out_act(self):
        # визначити, які канали є поточними
        current_channels = self.get_current_devices()
        for i in current_channels:
            # збільшення кількості лічильника
            super().out_act()
            # пристрій завершив роботу
            self.t_next[i] = float('inf')
            self.states[i] = 0
            if self.queue > 0:
                self.queue -= 1
                self.t_next[i] = self.t_curr + super().get_delay()
                self.states[i] = 1
            if self.next_element is not None:
                next_element = np.random.choice(a=self.next_element, p=self.probability)
                next_element.in_act()

        # region initial code
        # super().out_act()
        # super().set_t_next(float('inf'))
        # super().set_states([0])
        #
        # if self.get_queue() > 0:
        #     self.queue = self.queue - 1
        #     self.states = [1]
        #     self.t_next = self.t_curr + super().get_delay()
        # endregion

    def get_free_devices(self):
        free_devices = []
        for i in range(0, self.channel):
            if self.states[i] == 0:
                free_devices.append(i)
        return free_devices

    def get_current_devices(self):
        current_devices = []
        for i in range(0, self.channel):
            if self.t_next[i] == self.t_curr:
                current_devices.append(i)
        return current_devices

    def print_info(self):
        super().print_info()
        print('failure = {0}, length = {1}'.format(str(self.failure), str(self.queue)))

    def result(self, t_curr=0, i=0):
        super().result()
        mean_queue_counted, mean_load_counted = self.calculate_mean(self.t_curr)
        return {
            'Quantity' + str(i): self.quantity,
            'MeanQueue' + str(i): mean_queue_counted,
            'MeanLoad' + str(i): mean_load_counted,
            'Fails' + str(i): self.failure
        }

    def calculate_mean(self, t_curr):
        return self.mean_queue/t_curr, self.quantity/t_curr

    def calculate(self, delta):
        # для обчислення середнього значення довжини черги
        self.mean_queue = self.mean_queue + self.queue * delta

        # максимальне спостережуване значення черги
        if self.queue > self.max_observed_queue:
            self.max_observed_queue = self.max_queue
