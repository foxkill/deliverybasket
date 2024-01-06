#
# dlv:enums
#
from enum import Enum

class FutureMonths(Enum):
    """The monthcodes of future contracts"""
    F = 1
    G = 2
    H = 3
    J = 4
    K = 5
    M = 6
    N = 7
    Q = 8
    U = 9
    V = 10
    X = 11
    Z = 12

class FutureMonthsName(Enum):
    """The monthcodes of future contracts"""
    F = 'January'
    G = 'February'
    H = 'March'
    J = 'April'
    K = 'May'
    M = 'June'
    N = 'July'
    Q = 'August'
    U = 'September'
    V = 'October'
    Z = 'December'

class TreasuryFutures(Enum):
    TU =  2
    Z3N = 3
    FV = 5
    TY = 10
    TN = 11
    US = 20
    TWE = 21
    UL = 30