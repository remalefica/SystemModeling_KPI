from model import Model
from elements.create import Create
from elements.process import Process
from elements.dispose import Dispose

# region Task 5
c = Create(2.0)

p1 = Process(0.2)
p1.max_queue = 5

p2 = Process(20)
p2.max_queue = 5

p3 = Process(2.0)
p3.max_queue = 5

p4 = Process(2.0)
p4.max_queue = 5

d1, d2 = Dispose('DISPOSE1'), Dispose('DISPOSE2')

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [0.5, 0.5]
p2.next_element = [d1]
p3.next_element = [p4]
p4.next_element = [p1, d2]
p4.probability = [0.5, 0.5]

print('id0 = {0}, id1 = {1}, id2 = {2}, id3 = {3}, id4 = {4}'.format(
    c.id_el, p1.id_el, p2.id_el, p3.id_el, p4.id_el))

elements = [c, p1, p2, p3, p4, d1, d2]
model = Model(elements)
model.simulate(1000.0)

# endregion

# region Task from PR3
# c = Create(2.0)
# p = Process(1.0, 1)
#
# print('id0 = ' + str(c.get_id_el()) + '\t\tid1 = ' + str(p.get_id_el()))
#
# c.set_next_element(p)
# p.set_max_queue(5)
# c.set_name('CREATOR')
# p.set_name('PROCESSOR')
# c.set_distribution('exp')
# p.set_distribution('exp')
#
# el_list = [c, p]
# model = Model(el_list)
# model.simulate(1000.0)
# endregion