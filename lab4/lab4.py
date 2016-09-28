import sys
import regex as re
import random
import numpy as np
from collections import defaultdict

def main(args):
    if len(args) < 3:
        print('Usage: [-s | -l] filename [iterations | r]')
        sys.exit(0)
    G = defaultdict(list)
    filename = args[1]
    iterations = int(args[2])
    lines = open(filename).read().splitlines()
    V = int(lines[0])
    for i in range(int(lines[0])):
        G[i] = list()
    for l in lines[1:]:
        groups = re.findall(r'(\d\s\d)', l)
        for g in groups:
            t = g.split()
            v = int(t[0])
            e = int(t[1])
            G[v].append(e)
    print('Iterations: ' + str(iterations))
    if args[0] == '-s':
        a = 0.15
        
        A = np.zeros(shape=(V, V))
        for j in range(V):
            l = G[j]
            for i in range(V):
                if i in l:
                    A[i,j] = l.count(i)/len(l)
                else:
                    A[i,j] = 0

        p = np.array([1,0,0,0])
        B = np.full((V,V), a/V)

        M = (1-a)*A + B

        Q = M**iterations
        v1 = Q.dot(p)
        print(Q)
        print(v1)
    else:
        run(G, iterations)

def run(G, iterations):
    a = 85
    cur_node = 0
    visits = defaultdict(int)
    for i in range(iterations):
        r = random.randint(1,100)
        if r <= a:
            l = G[cur_node]
            if len(l):
                cur_node = random.choice(l)
                visits[cur_node] += 1
        else:
            cur_node = random.randint(0, len(G)-1)
            visits[cur_node] += 1
    
    N = sum(visits.values())
    print('Total visits: ' + str(N))
    for k in visits:
        v = visits[k]
        freq = v / N
        print('Node ' + str(k) + ':\t\t' + str(v) + ' at relative frequency: ' + str(freq))

if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)


