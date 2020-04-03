import uc
n = uc.net(3, 3, 2, 1)
a = [[1, 0, 0],
[0, 0, 1],
[1, 1, 0]]

b = [[1], [0], [1]]

soru = [1, 0, 1]

print n.tahmin(soru)
n.eg(a, b, 1000)
print n.tahmin(soru)
