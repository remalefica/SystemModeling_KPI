from random_1 import Random1
from random_2 import Random2
from random_3 import Random3

generator_1 = Random1(1/2, 10000)
generator_1.analyze(20)

generator_2 = Random2(2, 1, 10000)
generator_2.analyze(20)

generator_3 = Random3(10000)
generator_3.analyze(20)
