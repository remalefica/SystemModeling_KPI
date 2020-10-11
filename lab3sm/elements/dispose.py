import numpy as np
import element as e


class Dispose(e.Element):
    def __init__(self, name_of_element=None):
        super().__init__(0)
        self.name = 'DISPOSE' if name_of_element is None else name_of_element
        self.t_next = [float('inf')]

    def in_act(self):
        if self.states[0] == 0:
            self.states[0] = 1
            self.t_next[0] = self.t_curr + super().get_delay()  # set час звільнення пристрою

    def out_act(self):
        # збільшення кількості лічильника
        super().out_act()
        # пристрій завершив роботу
        self.t_next[0] = float('inf')
        self.states[0] = 0

    def print_info(self):
        print('{0}\tquantity = {1}'.format(str(self.name), str(self.quantity)))
