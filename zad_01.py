l = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print(l[0], l[-1])
print(len(l), max(l), min(l), sum(l), sorted(l))
l.append(6); print(l)
l.insert(2, 5); print(l)
l.extend([100, 200]); print(l)
l.remove(3); print(l)
print(l.pop(), l)
print(l.pop(0), l)
l.sort(); print(l)
l.reverse(); print(l)
a, b = [1, 2, 3], [4, 5]
print(a + b, a * 5)
c = a + b
print(c[:3], c[2:], c[1:5:2], c[::-1])
l.clear(); print(l)
