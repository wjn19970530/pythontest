# from decimal import Decimal
# a = Decimal.from_float(12.222)
# print(a)
# Decimal.getcontext().prec = 5
# a = Decimal("1")/Decimal("3")
# print(a)
# with Decimal.localcontext() as local:
#     local.prec=3
#     b = Decimal("10")/Decimal("3")
#     print(b)
from decimal import *
with localcontext() as local:
    local.prec=3
    b = Decimal("10")/Decimal("3")
    print(b)
a = Decimal("10")/Decimal("3")
print(a)