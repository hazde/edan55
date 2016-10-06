import sys
import regex as re
import random
import operator
import math
import numpy as np
from collections import defaultdict

def main(args):
    if len(args) < 3:
        print('Usage: filename [-s | -l] [iterations | r]')
        sys.exit(0)
    G = defaultdict(list)
    filename = args[0]
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
    if args[1] == '-l':
        a = 0.85
        vals = list()

        
        #H = np.zeros(shape=(V,V))
        """
        for k in G:
            l = G[k]
            for i in l:
                H[k, i] = l.count(i)/len(l)
        print(H)
        
        for j in range(V):
            l = G[j]
            cur = list()
            for i in range(V):
                if i in l:
                    cur.append(l.count(i)/len(l))
                else:
                    cur.append(0)
            vals.append(cur)
        H = np.matrix(vals)
        """
        #print(H)
        val = list()
        d_mul = 0
        for i in range(V):
            if len(G[i]):
                val.append([0 for i in range(V)])
            else:
                val.append([1/V for i in range(V)])
                d_mul += 1
        D = np.matrix(val)
        #print(D)
        h_mul = 0
        for k in G:
            l = G[k]
            for i in l:
                D[k, i] = l.count(i)/len(l)
                h_mul +=1

        p = np.full((V), 1/V)
        B = np.full((V,V), (1-a)/V)
        M = a*D + B
        print(p)
        
        diff = 1.0
        p_prev = p
        itr = 0
        while diff >= 0.01: 
            p = (p*M)
            diff_a = abs(p.A1 - p_prev)
            p_prev = p.A1
            diff = sum(diff_a)
            print(diff)
            itr += 1
            
        tot_mul = itr * V*V
        
        
        
        #print('Q:')
        print(itr)
        print('Pagerank vector:')
        print(np.sort(p.A1)[-5:])
        print(np.sum(p.A1))
        print('Multiplications: ' + str(tot_mul))
        
    elif args[1] == '-s':
        run(G, iterations)
    else:
        print('Unknown parameter ' + args[0])
        sys.exit(0)

def run(G, iterations):
    a = 85
    cur_node = 0
    visits = defaultdict(int)
    prev = defaultdict(int)
    
    diff = 1.0
    itr = 0
    while diff >= 0.01:
        r = random.randint(1,100)
        if r <= a:
            l = G[cur_node]
            if len(l):
                cur_node = random.choice(l)
                visits[cur_node] += 1
                if prev[cur_node] != 0:
                    diff = abs((prev[cur_node] - visits[cur_node]) / prev[cur_node])
                prev[cur_node] = visits[cur_node]
        else:
            cur_node = random.randint(0, len(G)-1)
            visits[cur_node] += 1
            if prev[cur_node] != 0:
                    diff = abs((prev[cur_node] - visits[cur_node]) / prev[cur_node])
            prev[cur_node] = visits[cur_node]
        #print(diff)
        itr += 1
    print(itr)
    """
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
    """
    N = sum(visits.values())
    #print('Total visits: ' + str(N))
    for k in visits:
        v = visits[k]
        freq = v / N
        print('Node ' + str(k) + ':\t\t' + str(v) + ' at relative frequency: ' + str(freq))
    s = sorted(visits.items(), key=operator.itemgetter(1))
    s = [(a[0], a[1] / N) for a in s]
    print(s[-5:])
if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)


