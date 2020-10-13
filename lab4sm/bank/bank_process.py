from universal_algorithm.elements.process import Process


class BankProcess(Process):
    def __init__(self, delay, channel=1, name_of_element=None):
        super().__init__(delay, channel, name_of_element)
        self.time_in_bank = 0.0
        self.interval_from_window = 0.0

    # to change
    def in_act(self):
        free_devices = self.get_free_devices()
        for i in free_devices:
            self.states[i] = 1
            self.t_next[i] = self.t_curr + super().get_delay()  # set час звільнення пристрою
            return self.t_next[i]
        else:
            if self.queue < self.max_queue:
                self.queue += 1
            else:
                self.failure += 1


