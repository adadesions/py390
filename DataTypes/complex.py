"""
    Complex Number in Python
    'complex number = Real part + Imagine part'
"""
print('Complex Number!')
print('{} is {}'.format(9+2j, type(9+2j)))

# Arithmetic
print((1+2j)+(2+3j))
print((1+2j)-(2+3j))
print((1+2j)*(2+3j))
print((1+2j)/(2+3j))

# get Real and imagine part separately
comx = 88+92j
print('Real part = {}'.format(comx.real))
print('Imagine part = {}'.format(comx.imag))
print('Conjugation = {}'.format(comx.conjugate()))

# Problem
# Solve (i^10 - i)/(2i + 1)
print('Problem!')
numerator = 10j ** 10 - 1j
denominator = 2j + 1
print('Answer = {}'.format(numerator/denominator))
