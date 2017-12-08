from collections import defaultdict


def t(var, cond, val):
    if cond == '>':
        return reg[var] > int(val)
    if cond == '<':
        return reg[var] < int(val)
    if cond == '>=':
        return reg[var] >= int(val)
    if cond == '<=':
        return reg[var] <= int(val)
    if cond == '==':
        return reg[var] == int(val)
    if cond == '!=':
        return reg[var] != int(val)
    raise Exception('bad')

ops = {
    'INC': 1,
    'DEC': -1,
}
reg = defaultdict(lambda: 0)
mreg = defaultdict(lambda: 0)

with open('input') as f:
    lines = map(str.strip, f.readlines())

lines = [line.upper().split() for line in lines]
for line in lines:
    if t(*line[4:]):
        reg[line[0]] += ops[line[1]] * int(line[2])
        if(reg[line[0]] > mreg[line[0]]):
            mreg[line[0]] = reg[line[0]]


#solution 1
print('solution 1: %s' % max(reg.values()))

#solution 2
print('solution 2: %s' % max(mreg.values()))
