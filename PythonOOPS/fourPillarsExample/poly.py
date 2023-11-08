from SA import *
from CA import *


def get_service(obj):
    print(obj.cal_bal())


get_service(SA(4, 'Mounika', 'mouni@gmail.com', 'vijawada', 10000))
get_service(CA(3, 'srinivas', 'srinu@gmail.com', 'guntur', 30000))
get_service(Account('gopi', 'gopi@academy.com', 'Hyd'))