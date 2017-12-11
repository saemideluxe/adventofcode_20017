def part1():
    with open('input') as f:
        _in = list(map(int, f.read().strip().split(',')))

    l = 256
    rope = list(range(l))
    pos = 0
    skip = 0

    for length in _in:
        pos %= l
        for i in range(length//2):
            tmp = rope[(pos + i) % l]
            rope[(pos + i) % l] = rope[(pos + length - 1 - i) % l]
            rope[(pos + length - 1 - i) % l] = tmp
        pos += length + skip
        skip += 1

    print('solution 1: %s' % (rope[0] * rope[1]))

#------------------------------------------------------------------

def part2():
    with open('input') as f:
        _in = f.read().strip()
    numbers = list(map(ord, _in)) +  [17, 31, 73, 47, 23]

    l = 256
    rope = list(range(l))
    pos = 0
    skip = 0

    for k in range(64):
        for length in numbers:
            pos %= l
            for i in range(length//2):
                tmp = rope[(pos + i) % l]
                rope[(pos + i) % l] = rope[(pos + length - 1 - i) % l]
                rope[(pos + length - 1 - i) % l] = tmp
            pos += length + skip
            skip += 1

    _hash = []
    for m in range(16):
        h = rope[m * 16]
        for j in range(15):
            h ^= rope[m * 16 + 1 + j]
        _hash.append(h)

    result = ''.join(map(lambda a: '%02x' % a,_hash))
    print('solution 2 %s' % result)


part1()
part2()
