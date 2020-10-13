import pandas as pd
from tabulate import tabulate

from elements.create import Create
from elements.process import Process
from elements.dispose import Dispose
from element import Element
from model import Model

rows = []


def new_test(cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, smo4d, smo4l, smo4p, prob, time):
    c = Create(cr)

    p1 = Process(smo1p, smo1d)
    p1.max_queue = smo1l

    p2 = Process(smo2p, smo2d)
    p2.max_queue = smo2l

    p3 = Process(smo3p, smo3d)
    p3.max_queue = smo3l

    p4 = Process(smo4p, smo4d)
    p4.max_queue = smo4l

    d1, d2 = Dispose('DISPOSE1'), Dispose('DISPOSE2')

    c.next_element = [p1]
    p1.next_element = [p2, p3]
    p1.probability = [prob, 1 - prob]
    p2.next_element = [d1]
    p3.next_element = [p4]
    p4.next_element = [p1, d2]
    p4.probability = [prob, 1 - prob]

    print('id0 = {0}, id1 = {1}, id2 = {2}, id3 = {3}, id4 = {4}'.format(
        c.id_el, p1.id_el, p2.id_el, p3.id_el, p4.id_el))

    elements = [c, p1, p2, p3, p4, d1, d2]
    model = Model(elements)
    res, pro = model.simulate(time, False)

    Element.nextId = 0
    param = {'CrDelay': cr,
             'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
             'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
             'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
             'PrDelay4': smo4p, 'QLimit4': smo4l, 'Devices4': smo4d,
             '%': prob}

    rows.append({**param, **res, **pro})
    del c, p1, p2, p3, p4, d1, d2, model, param, res, pro, elements


# region 0: Головний
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 1: середній інтервал надходження вимог +2
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(4.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 2: середній інтервал надходження вимог -1
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(1.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 3: середня тривалість обслуговування в СМО1 +3.5
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 5.5, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 4: середня тривалість обслуговування в СМО1 -1.5
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 0.5, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 5: обмеження на довжину черги СМО1 +4
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 9, 2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 6: обмеження на довжину черги СМО1 -4
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 1, 2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 7: кількість пристроїв в СМО1 +3
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 4, 5, 2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 8: середня тривалість обслуговування в СМО2 +3.0
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 5.0, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 9: середня тривалість обслуговування в СМО2 -1.5
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 0.5, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 10: обмеження на довжину черги СМО2 +3
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 8, 2.0, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 11: обмеження на довжину черги СМО2 -3
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 2, 2.0, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 12: кількість пристроїв в СМО2 +3
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 4, 5, 2.0, 1, 5, 2.0, 1, 5, 2, 0.5, 1000)
# endregion

# region 13: середня тривалість обслуговування в СМО3 +1.5
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 3.5, 1, 5, 2, 0.5, 1000)
# endregion

# region 14: середня тривалість обслуговування в СМО3 -1.9
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 0.1, 1, 5, 2, 0.5, 1000)
# endregion

# region 15: обмеження на довжину черги СМО3 +4
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 8, 2.0, 1, 5, 2.0, 0.5, 1000)
# endregion

# region 16: обмеження на довжину черги СМО3 -4
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 1, 2.0, 1, 5, 2.0, 0.5, 1000)
# endregion

# region 17: кількість пристроїв в СМО3 +3
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 4, 5, 2.0, 1, 5, 2.0, 0.5, 1000)
# endregion

# region 18: середня тривалість обслуговування в СМО4 +1.5
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 3.5, 0.5, 1000)
# endregion

# region 19: середня тривалість обслуговування в СМО4 -1.9
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 0.9, 0.5, 1000)
# endregion

# region 20: обмеження на довжину черги СМО4 +4
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 9, 2, 0.5, 1000)
# endregion

# region 21: обмеження на довжину черги СМО4 -4
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 1, 2, 0.5, 1000)
# endregion

# region 22: кількість пристроїв в СМО4 +2
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 4, 5, 2.0, 3, 5, 2, 0.5, 1000)
# endregion

# region 23: ймовірність +0.3
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2, 0.8, 1000)
# endregion

# region 24: ймовірність -0.4
# cr, smo1d, smo1l, smo1p, smo2d, smo2l, smo2p, smo3d, smo3l, smo3p, 1, 5, 2, prob, time
new_test(2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2.0, 1, 5, 2, 0.1, 1000)
# endregion

df = pd.DataFrame()
df = df.append(rows)
print(tabulate(df, headers='keys', tablefmt='fancy_grid', numalign="center"))
