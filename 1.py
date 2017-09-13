import numpy as np
import re
from numpy.linalg import norm

def cos_dist(a, b):
    skalar_proizv = np.dot(a, b)
    n_a = norm(a, ord=2)
    n_b = norm(b, ord=2)
    return skalar_proizv/(n_a*n_b)


dictionary = {}

sentences = open('sentences.txt', 'r')
d = -1
n = 0
text_list = []
for line in sentences:
    n += 1
    line = line.lower()
    line = re.split(r'[^a-z]', line)
    text_list.append(line)
    for word in line:
        if word not in dictionary and word != '':
            d += 1
            dictionary[word] = d
sentences.close()
matrix = np.array([[0] * (d + 1) for i in np.arange(n)])
ind = 0
for line in text_list:
    for word in line:
        if word != '':
            matrix[ind][dictionary[word]] = line.count(word)
    ind += 1

a = matrix[0]
res = []
for ind in np.arange(1, len(matrix)):
    b = matrix[ind]
    res.append(cos_dist(a, b))
k = res.index(max(res))
res.pop(k)
l = res.index(max(res))
if l >= k:
    l += 1
wr = open('submission-1.txt', 'w')
wr.write(str(k+1))
wr.write(' ')
wr.write(str(l+1))
wr.close()


