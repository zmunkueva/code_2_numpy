import numpy as np
#работа с действительными числами
str =  open("real-numbers.txt").read().split('\n')
arr = np.array([float(f) for f in str])
print('real numbers\nmax = ', np.max(arr))
print('min = ', np.min(arr))
print('mean = ', np.mean(arr))
print('rms = ', np.std(arr))
from scipy import stats
print('5 moment = ', stats.moment(arr, moment = 5), '\n')

#целые числа
str_n = open("integer.txt").read().split('\n')
arr_n = np.array([int(n) for n in str_n])
print('integer\nsorted: ', np.sort(arr_n), '\n')

#работа с комплексными числами
str_c = open("complex.txt").read().split('\n')
arr_c = [complex(c) for c in str_c]
print('complex numbers\nsorted by module: ', sorted(arr_c, key = abs), '\n')
print('sorted by real part: ', sorted(arr_c,  key = lambda c: c.real, reverse=True), '\n')
#список строк
str_s = open("string.txt").read().split()
print('strings\n', str_s)
def sorted(str_s):
    str_s.sort(key = len)
    return str_s
print('sorted: ', sorted(str_s), '\n')

#кортеж слов в лесикографическом порядке
array = open("tuple.txt").read().split('\n')
tpl = tuple(array)
print('tuple\n', tpl)
tpl = tuple(np.sort(tpl))
print('sorted: ', tpl)
