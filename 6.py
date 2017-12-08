#------------------------------------------------------------

# here is solution 1:
n = 0
seen = set()
with open('input') as f:
    slots = list(map(int, f.read().strip().split()))

while not tuple(slots) in seen:
    seen.add(tuple(slots))
    _max = max(slots)
    i = slots.index(_max)
    slots[i] = 0
    for j in range(_max):
        slots[(i + 1 + j) % len(slots)] += 1
    n += 1

print('solution 1: %s' % n)

#------------------------------------------------------------

# and here is solution 2:
n = 0
seen = set()
target = tuple(slots)
while not ((tuple(slots) in seen) and (target == tuple(slots))):
    seen.add(tuple(slots))
    _max = max(slots)
    i = slots.index(_max)
    slots[i] = 0
    for j in range(_max):
        slots[(i + 1 + j) % len(slots)] += 1
    n += 1

print('solution 2: %s' % n)

#------------------------------------------------------------
