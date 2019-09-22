"""
Floating-Point: IEEE 754
https://en.wikipedia.org/wiki/IEEE_754-2008_revision
1.8 ⨉ 10^308
"""
print('Floating-Point: IEEE 754')
print('{} is {}'.format(9.2, type(9.2)))

# Scientific Notation
# 1e3 = 1x10^3
# 2e-2 = 2x10^(-2)
print('Scientific Notation')
print('1e3 = {}, {}'.format(1e3, type(1e3)))
print('2e-2 = {}, {}'.format(2e-2, type(2e-2)))
print('10e2 = {}, {}'.format(10e2, type(10e2)))
print('Max value of double precision: {}'.format(1.79e308))
print('Out of range: {}'.format(1.8e308))