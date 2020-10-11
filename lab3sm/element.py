import fun_rand as fr
from termcolor import colored


class Element:
    nextId = 0

    def __init__(self, delay=None, name_of_element=None):
        self.t_next = [0.0]         # момент часу наступної події
        self.delay_mean = 1.0       # середнє значення часової затримки
        self.delay_dev = None       # середнє квадратичне відхилення часової затримки
        self.quantity = 0
        self.t_curr = 0.0           # поточний момент часу
        self.states = [0]
        self.next_element = None    # вказує на наступний (в маршруті слідування вимоги) елемент моделі
        self.id_el = Element.nextId
        Element.nextId += 1
        self.probability = [1]
        self.distribution = 'exp'

        if delay is None and name_of_element is None:
            self.name = 'element' + str(self.id_el)
        else:
            self.delay_mean = delay
            if name_of_element is None:
                self.name = 'anonymous'
            else:
                self.name = str(name_of_element)

    def get_delay(self):
        delay = self.delay_mean
        if 'exp' == self.distribution.lower():
            delay = fr.exp(self.delay_mean)
        elif 'norm' == self.distribution.lower():
            delay = fr.norm(self.delay_mean, self.delay_dev)
        elif 'unif' == self.distribution.lower():
            delay = fr.unif(self.delay_mean, self.delay_dev)
        else:
            delay = self.delay_mean
        return delay

    def get_name(self):
        return self.name

    def in_act(self):  # вхід в елемент
        pass

    def out_act(self):  # вихід з елементу
        self.quantity += 1

    def result(self, t_curr=0, i=0):
        print('\n{0}\nquantity = {1}'.format(colored(self.name, 'cyan'), str(self.quantity)))
        return self.quantity

    def print_info(self):
        print(self.name + '\tstate = ' + str(self.states) +
              '\tquantity = ' + str(self.quantity) +
              '\tt_next = ' + str(self.t_next))

    def calculate(self, delta):
        pass

    def calculate_mean(self, delta):
        pass
