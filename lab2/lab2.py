import regex as re
import random as rnd
import sys
from collections import defaultdict

file = "pw09_100.9.txt"
if len(sys.argv) > 1: file = sys.argv[1]

lines = re.split(r'\n', open(file).read())
edges = defaultdict(tuple)

info = re.split(r'\s', lines[0])
v_count = info[0]


def flip(p):
    return 0 if rnd.uniform(0.0, 1.0) < p else 1


def run():
    totsum = 0
    for t in lines[1:]:
        vals = re.split(r'\s', t)
        
        if len(vals) > 1:
            edges[tuple(vals[:2])] = vals[2]
            totsum += int(vals[2])
    
    print(totsum)
    print(totsum/2)
    
    cut = dict()
    for i in range(int(v_count)):
        if flip(0.5):
            cut[str(i)] = i

    maxcut = 0
    for t in edges:
        if (t[0] in cut and t[1] not in cut) or (t[0] not in cut and t[1] in cut):
            maxcut += int(edges[(t[0], t[1])])
    return maxcut

run()
"""
tot = 0
iterations = 100
for i in range(0, iterations):
    thisrun = run()
    print(thisrun)
    tot += thisrun
tot /= iterations
"""
#print(tot)

