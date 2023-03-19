import random
import string
import sys


Float32Array = "new Float32Array(["
Back = "])"

count = 10 # default
numbers = 2000 # default
if len(sys.argv) == 3:
    count = int(sys.argv[1])
    numbers = int(sys.argv[2])

x = []
y = []

print("var rand_scatters_x = {};")
print("var rand_scatters_y = {};")
for _ in range(count):
    letters = string.ascii_lowercase
    key = ''.join(random.choice(letters) for _ in range(count))
    for _ in range(numbers):
        x.append(round(random.uniform(0, 101), 4)) # rand float
        y.append(round(random.uniform(0, 101), 4))
    print("rand_scatters_x['",key ,"'] = ", Float32Array, sep='', end='')
    print(*x, sep=', ', end='')
    print(Back, ";", sep='')

    print("rand_scatters_y['",key ,"'] = ", Float32Array, sep='', end='')
    print(*y, sep=', ', end='')
    print(Back, ";", sep='')

    # clear x and y
    x = []
    y = []

"""
print("console.log('rand_scatters_x', rand_scatters_x);")
print("console.log('rand_scatters_y', rand_scatters_y);")
"""
