import numpy as np
import matplotlib.pyplot as plt


# 标准化
def z_score(x):
    '''x∗=(x−μ)/σ'''
    x_mean = np.mean(x)
    s2 = sum([(i - np.mean(x)) * (i - np.mean(x)) for i in x]) / len(x)
    return [(i - x_mean) / s2 for i in x]


li = [-15, 15, 15, 26, 23, 45, 7, 12, 22, 11, 8, 8, 23, 44, 56, 89, 9, 9, 6, 12, 9, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 12, 34,
     27, 12, 12, 12, 12, 12, 16, 13, 13, 15, 14, 34, 23, 11, 22, 68]
# li = [-10, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11,
#       11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 30]
cs = []
for i in li:
    c = li.count(i)
    cs.append(c)
print(cs)
z = z_score(li)
print(z)
plt.plot(z, cs)
plt.show()
