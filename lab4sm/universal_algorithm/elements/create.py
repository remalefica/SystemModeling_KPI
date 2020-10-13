from universal_algorithm import element as e


class Create(e.Element):
    def __init__(self, delay, name_of_element=None):
        super().__init__(delay)
        self.name = 'CREATOR' if name_of_element is None else name_of_element

    def out_act(self):
        # виконуємо збільшення лічильника кількості
        super().out_act()

        # встановлюємо коли пристрій буде вільним
        self.t_next[0] = self.t_curr + super().get_delay()  # встановлюємо час звільнення пристрою
        super().choose_next_element()
