# copied from https://www.reddit.com/r/adventofcode/comments/7izym2/2017_day_11_solutions/
# with slight modifications

def dist(x, y):
    if abs(y) > (abs(x)*.5):
        return int(abs(y)-(abs(x)*.5)+abs(x))
    else:
        return int(abs(x))

with open('input') as file:
    _in = file.readline().strip().split(',')

directions = {
    'n':  (0, 1),
    's':  (0, -1),
    'ne': (1, .5),
    'se': (1, -.5),
    'nw': (-1, .5),
    'sw': (-1, -.5)
}

x = 0
y = 0
_max = 0

for i in _in:
    x += directions[i][0]
    y += directions[i][1]
    if _max < dist(x,y):
        _max = dist(x,y)

print('Solution 1: ' + str(dist(x,y)))
print('Solution 2: ' + str(_max))
