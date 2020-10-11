import numpy as np
import element as e


class Create(e.Element):
    def __init__(self, delay):
        super().__init__(delay)
        self.name = 'CREATOR'

    def out_act(self):
        # виконуємо збільшення лічильника кількості
        super().out_act()
        # встановлюємо коли пристрій буде вільним
        self.t_next[0] = self.t_curr + super().get_delay()  # встановлюємо час звільнення пристрою
        next_element = np.random.choice(a=self.next_element, p=self.probability)
        next_element.in_act()
