from collections import Counter
d = Counter()
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d.most_common(1))
print(d.most_common(2))


# or
f = {
    'a': 5,
    'b': 4,
    'c': 3
}
f = Counter(f)
print(f.most_common(1))
print(f.most_common(2))