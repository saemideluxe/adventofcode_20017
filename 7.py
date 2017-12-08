#------------------------------------------------------------

# here is solution 1:
nodes = set()
hasparent = set()
with open('input') as f:
    lines = map(str.strip, f.readlines())
    for line in lines:
        s = line.split()
        node = s[0]
        children = s[3:]
        nodes.add(node)
        for c in children:
            hasparent.add(c.replace(',', ''))

for n in nodes:
    if n not in hasparent:
        root = n
        print('solution 1: %s' % n)

#------------------------------------------------------------

# here is solution 2:
nodes = {}
with open('input') as f:
    lines = map(str.strip, f.readlines())
    for line in lines:
        s = line.split()
        node = s[0]
        children = s[3:]
        nodes[node] = [int(s[1][1:-1])]
        for c in children:
            nodes[node].append(c.replace(',', ''))

def check(disk):
    sums = {}
    for i in nodes[disk][1:]:
        sums[i] = check(i)
    if len(set(sums.values())) > 1:
        counter = {x: [] for x in sums.values()}
        for child,childsum in sums.items():
            counter[childsum].append(child)
        for childsum,childlist in counter.items():
            if len(childlist) == 1:
                bad = childlist[0]
            if len(childlist) > 1:
                good = childlist[0]
        raise Exception('solution 2: %s' % (nodes[bad][0] + sums[good] - sums[bad]))

    return sum(sums.values()) + nodes[disk][0]

try:
    check(root)
except Exception as e:
    print(str(e))

#------------------------------------------------------------
