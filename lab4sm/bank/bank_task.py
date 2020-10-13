from bank.bank_model import BankModel
from bank.bank_create import BankCreate
from bank.bank_process import BankProcess
from universal_algorithm.elements.dispose import Dispose


def task_bank():
    c = BankCreate(0.5)

    p1 = BankProcess(0.3, name_of_element='CASHIER1')
    p1.max_queue = 3

    p2 = BankProcess(0.3, name_of_element='CASHIER2')
    p2.max_queue = 3

    d1 = Dispose('DISPOSE')

    c.next_element = [p1, p2]
    c.priority = [1, 2]                 # 1ий пріоритет у першої смуги
    p1.next_element = [d1]
    p2.next_element = [d1]

    elements = [c, p1, p2, d1]
    model = BankModel(elements)
    model.allowed_transfers = [p1, p2]
    model.transfer_condition = 2
    model.simulate(1000.0, flag=True)
