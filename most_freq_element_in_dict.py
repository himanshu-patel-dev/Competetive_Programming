d = {
    'a': 1,
    'b': 2,
    'c': 3
}
from collections import Counter
d = Counter(d)
print(d.most_common(1))
print(d.most_common(2))
