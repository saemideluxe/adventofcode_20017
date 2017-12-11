with open('input') as f:
    _in = f.read().strip()

score = 0
level = 0
ignorenext = False
ingarbage = False
garbage = 0

for c in _in:
    if not ingarbage:
        if c == '{':
            level += 1
        elif c == '}':
            score += level
            level -= 1
        elif c == '<':
            ingarbage = True
    else:
        if not ignorenext:
            if c == '>':
                ingarbage = False
            elif c == '!':
                ignorenext = True
            else:
                garbage += 1
        else:
            ignorenext = False


print('solution 1: %s' % score)
print('solution 2: %s' % garbage)
