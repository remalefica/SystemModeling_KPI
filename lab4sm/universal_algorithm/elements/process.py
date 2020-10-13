from universal_algorithm import element as e


class Process(e.Element):
    def __init__(self, delay, channel=1, name_of_element=None):
        super().__init__(delay)
        self.name = 'PROCESSOR' + str(self.id_el) if name_of_element is None else name_of_element
        self.queue, self.max_observed_queue = 0, 0
        self.max_queue = float('inf')
        self.mean_queue = 0.0
        self.failure = 0
        self.channel = channel
        self.t_next = [float('inf')] * self.channel
        self.states = [0] * self.channel
        self.mean_load = 0

    def in_act(self):
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
                super().choose_next_element()

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
        return self.mean_queue/t_curr, self.mean_load/t_curr

    def calculate(self, delta):
        # для обчислення середнього значення довжини черги
        self.mean_queue += self.queue * delta

        for i in range(self.channel):
            self.mean_load += self.states[i] * delta

        # максимальне спостережуване значення черги
        if self.queue > self.max_observed_queue:
            self.max_observed_queue = self.max_queue
