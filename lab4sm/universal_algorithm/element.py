from universal_algorithm import fun_rand as fr
from termcolor import colored
from copy import deepcopy
import numpy as np


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
        self.distribution = 'exp'
        self.probability = [1]      # ймовірність обрання СМО - масив, сума елементів якого == 1
        self.priority = [1]         # пріоритет обрання СМО - масив, де 1 - це пріоритетне СМО

        if delay is None and name_of_element is None:
            self.name = 'element' + str(self.id_el)
        else:
            self.delay_mean = delay
            if name_of_element is None:
                self.name = 'anonymous'
            else:
                self.name = str(name_of_element)

    def get_delay(self):
        if 'exp' == self.distribution.lower():
            delay = fr.exp(self.delay_mean)
        elif 'norm' == self.distribution.lower():
            delay = fr.norm(self.delay_mean, self.delay_dev)
        elif 'unif' == self.distribution.lower():
            delay = fr.unif(self.delay_mean, self.delay_dev)
        elif 'erlang' == self.distribution.lower():
            delay = fr.erlang(self.delay_mean, self.delay_dev)
        elif 'empirical' == self.distribution.lower():
            delay = fr.empirical(self.delay_mean, self.delay_dev)
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

    def choose_next_element(self):
        # пріоритетність чи ймовірність
        if self.probability != [1] and self.priority != [1]:
            raise Exception('Route selection is ambiguous: probability and priority are set simultaneously')
        elif self.probability != [1]:
            next_element = np.random.choice(a=self.next_element, p=self.probability)
            next_element.in_act()
        elif self.priority != [1]:
            next_element = self.choose_by_priority()
            next_element.in_act()
        elif self.probability == [1] and self.priority == [1]:
            self.next_element[0].in_act()

    def choose_by_priority(self):
        priorities = deepcopy(self.priority)
        min_queue = float('inf')
        min_queue_index = 0

        for p in range(len(priorities)):
            if min(priorities) == 100000:
                break

            # find element by max priority
            max_pr_index = priorities.index(min(priorities))
            # при рівній довжині черг, а також при відсутності черг, віддається перевага пріоритетному маршруту
            # якщо є вільні пристрої
            if 0 in self.next_element[max_pr_index].states:
                return self.next_element[max_pr_index]
            else:
                if self.next_element[max_pr_index].queue < min_queue:
                    min_queue = self.next_element[max_pr_index].queue
                    min_queue_index = self.next_element.index(self.next_element[max_pr_index])

            # remove from priorities by setting big int value
            priorities[max_pr_index] = 100000

        return self.next_element[min_queue_index]
