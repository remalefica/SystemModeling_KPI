import pandas as pd
from tabulate import tabulate

from elements.create import Create
from elements.process import Process
from elements.dispose import Dispose
from element import Element
from model import Model

rows = []

cr, smo1d, smo1l, smo1p, prob, time = 2.0, 5, 3, 3.5, 0.5, 1000
smo2d, smo2l, smo2p = 7, 5, 2.5
smo3d, smo3l, smo3p = 2, 2, 3.0

# region 0: Головний
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 1: середній інтервал надходження вимог +2
c = Create(cr + 2.0)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr + 2.0, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 2: середній інтервал надходження вимог -1
c = Create(cr - 1.0)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr - 1.0, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 3: середня тривалість обслуговування в СМО1 +3.5
c = Create(cr)

p1 = Process(smo1p + 3.5, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p + 3.5, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 4: середня тривалість обслуговування в СМО1 -2.5
c = Create(cr)

p1 = Process(smo1p - 2.5, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p - 2.5, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 5: обмеження на довжину черги СМО1 +4
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l + 4

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l + 4, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 6: обмеження на довжину черги СМО1 -2
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l - 2

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l - 2, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 7: кількість пристроїв в СМО1 +3
c = Create(cr)

p1 = Process(smo1p, smo1d + 3)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d + 3,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 8: кількість пристроїв в СМО1 -3
c = Create(cr)

p1 = Process(smo1p, smo1d - 3)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d - 3,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 9: середня тривалість обслуговування в СМО2 +3.0
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p + 3.0, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p + 3.0, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 10: середня тривалість обслуговування в СМО2 -1.5
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p - 1.5, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p - 1.5, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 11: обмеження на довжину черги СМО2 +3
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l + 3

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l + 3, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 12: обмеження на довжину черги СМО2 -3
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l - 3

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l - 3, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 13: кількість пристроїв в СМО2 +3
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d + 3)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d + 3,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 14: кількість пристроїв в СМО2 -5
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d - 5)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d - 5,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 15: середня тривалість обслуговування в СМО3 +1.5
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p + 3.0, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p + 3.0, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 16: середня тривалість обслуговування в СМО3 -2.9
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p - 2.9, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p - 2.9, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 17: обмеження на довжину черги СМО3 +4
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l + 4

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]

elements = [c, p1, p2, p3]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l + 4, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, model, param, res, pro, elements
# endregion

# region 18: обмеження на довжину черги СМО3 -1
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l - 1

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l - 1, 'Devices3': smo3d,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 19: кількість пристроїв в СМО3 +3
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d + 3)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d + 2,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 20: кількість пристроїв в СМО3 -1
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l - 1

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob, 1 - prob]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]
model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d - 1,
         '%': prob}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 21: ймовірність +0.3
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob + 0.3, 1 - prob - 0.3]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]

model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob + 0.3}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

# region 22: ймовірність -0.4
c = Create(cr)

p1 = Process(smo1p, smo1d)
p1.max_queue = smo1l

p2 = Process(smo2p, smo2d)
p2.max_queue = smo2l

p3 = Process(smo3p, smo3d)
p3.max_queue = smo3l

d = Dispose()

c.next_element = [p1]
p1.next_element = [p2, p3]
p1.probability = [prob - 0.4, 1 - prob + 0.4]
p2.next_element = [d]
p3.next_element = [d]

elements = [c, p1, p2, p3, d]

model = Model(elements)
res, pro = model.simulate(time, False)

Element.nextId = 0
param = {'CrDelay': cr, 'Distribution': 'exp', 'TimeModeling': time,
         'PrDelay1': smo1p, 'QLimit1': smo1l, 'Devices1': smo1d,
         'PrDelay2': smo2p, 'QLimit2': smo2l, 'Devices2': smo2d,
         'PrDelay3': smo3p, 'QLimit3': smo3l, 'Devices3': smo3d,
         '%': prob - 0.4}

rows.append({**param, **res, **pro})
del c, p1, p2, p3, d, model, param, res, pro, elements
# endregion

df = pd.DataFrame()
df = df.append(rows)
print(tabulate(df, headers='keys', tablefmt='fancy_grid', numalign="center"))
