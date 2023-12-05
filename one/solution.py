import re
 
with open('./input.txt') as f:
    sum = 0
    for line in f:
        v = list(re.sub(r'[^0-9]', "", line))

        sum += int(v[0] + v[-1])
    
    print("Part one: %d" % (sum))