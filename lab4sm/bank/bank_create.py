from universal_algorithm.elements.create import Create
import numpy as np


class BankCreate(Create):
    def __init__(self, delay, name_of_element=None):
        super().__init__(delay, name_of_element)

    def out_act(self):
        # виконуємо збільшення лічильника кількості
        self.quantity += 1
        # встановлюємо коли пристрій буде вільним
        self.t_next[0] = self.t_curr + super().get_delay()  # встановлюємо час звільнення пристрою

        # пріоритетність чи ймовірність
        if self.probability != [1] and self.priority != [1]:
            raise Exception('Route selection is ambiguous: probability and priority are set simultaneously')
        elif self.probability != [1]:
            next_element = np.random.choice(a=self.next_element, p=self.probability)
            return next_element.in_act()
        elif self.priority != [1]:
            next_element = self.choose_by_priority()
            return next_element.in_act()
        elif self.probability == [1] and self.priority == [1]:
            return self.next_element[0].in_act()
