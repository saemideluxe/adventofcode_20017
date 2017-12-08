#------------------------------------------------------------

# here is solution 1:
myinput = open('input')
lines = map(str.strip, myinput.readlines())
lines = map(int, lines)
lines = list(lines)

i = 0
n = 0
while 0 <= i < len(lines):
    old = i
    i += lines[i]
    lines[old] += 1
    n += 1

print('solution 1: %s' % n)

#------------------------------------------------------------

# and here is solution 2:
myinput = open('input')
lines = map(str.strip, myinput.readlines())
lines = map(int, lines)
lines = list(lines)

i = 0
n = 0
while 0 <= i < len(lines):
    old = i
    oldv = lines[i]
    i += lines[i]
    if oldv >= 3:
        lines[old] -= 1
    else:
        lines[old] += 1
    n += 1

print('solution 2: %s' % n)

#------------------------------------------------------------
