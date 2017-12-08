#------------------------------------------------------------

# here is solution 1:
myinput = open('input.txt')
lines = myinput.readlines()
validlines = 0

for line in lines:
    words = line.split()
    isvalid = True
    for word in words:
        countword = words.count(word)
        if countword > 1:
            isvalid = False

    if isvalid:
        validlines = validlines + 1

print('solution 1 is: %s' % validlines)


#------------------------------------------------------------

# and here is solution 2:
myinput = open('input.txt')
lines = myinput.readlines()
validlines = 0

for line in lines:
    words = [''.join(sorted(word)) for word in line.split()]
    isvalid = True
    for word in words:
        countword = words.count(word)
        if countword > 1:
            isvalid = False

    if isvalid:
        validlines = validlines + 1

print('solution 2 is: %s' % validlines)

#------------------------------------------------------------
