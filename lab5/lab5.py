import sys
import operator
import time
from collections import defaultdict
from itertools import chain, combinations


def main(args):
    if len(args) < 1:
        print('Usage: python lab5.py filename (w/o file extension)')
        sys.exit(0)
    
    files = [args[0] + '.gr', args[0] + '.td']
    parse(files)



def parse(files):
    #d = 'data/'
    g_rows = open(files[0]).read().split('\n')
    t_rows = open(files[1]).read().split('\n')
    G = defaultdict(list)
    T_b = defaultdict(set)
    T_n = defaultdict(list)
    T_t = defaultdict(dict)
    g_nodes = ''
    for r in g_rows:
        if len(r) > 0:
            if r[0] == 'p':
                g_nodes = int(r.split()[2])
                for i in range(1, g_nodes+1):
                    G[i] = []
            elif r[0] == 'c':
                pass
            else:
                edge = r.split()
                if int(edge[0]) > g_nodes or int(edge[1]) > g_nodes:
                    print('Invalid edge: ' + edge[0] + ' -> ' + edge[1])
                    sys.exit(0)
                G[int(edge[0])].append(int(edge[1]))
                G[int(edge[1])].append(int(edge[0]))
    bags = tw = ''
    for r in t_rows:
        if len(r) > 0:
            if r[0] == 's':
                bags = int(r.split()[2])
                tw = int(r.split()[3])
                
            elif r[0] == 'b':
                nodes = [int(n) for n in r.split()[1:]]
                s_set = frozenset(nodes[1:])
                T_t[nodes[0]] = {k:0 for k in powerset(s_set)}
                T_b[nodes[0]] = s_set
            elif r[0] == 'c':
                pass
            else:
                edge = r.split()
                if int(edge[0]) > g_nodes or int(edge[1]) > g_nodes:
                    print('Invalid edge: ' + edge[0] + ' -> ' + edge[1])
                    sys.exit(0)
                T_n[int(edge[0])].append(int(edge[1]))
                T_n[int(edge[1])].append(int(edge[0]))

    root = min(T_n, key= lambda x: len(T_n[x]))
    visited = {k:False for k in T_n}
    l = list()
    build_list(l, T_n, root, visited)
    #print(l)
    #print(G)
    #print(independent(frozenset([1,3,5]), G))
    first = time.clock()
    run(T_b, T_n, T_t, G, l)
    print((time.clock() - first))

def build_list(l, T_n, node, visited):
    if visited[node]:
        pass
    else:
        visited[node] = True
        for c in T_n[node]:
            build_list(l, T_n, c, visited)
        l.append(node)
        
        

def run(T_b, T_n, T_t, G, l):
    root = l[len(l)-1]
    for i in l:
        if len(T_n[i]) == 1 and i != root:       # Check for leaves
            for s in T_t[i]:
                if independent(s, G):
                    T_t[i][s] = len(s)
            #print('Bag: ' + str(i))
            #print(T_t[i])
        else:
            for u in T_t[i]:
                if independent(u, G):
                    T_t[i][u] = len(u) + maxsum(T_n[i], T_t, T_b, u, i)
    m = T_t[root]
    s = max(m.items(), key=operator.itemgetter(1))
    print(s)
    print(max(m.values()))

def maxsum(ninjos, T_t, T_b, u, node):
    t_list = list()
    for n in ninjos:
        u_list = list()
        for ui in T_t[n]:
            size = T_t[n][ui]  # U_i  
            if size > 0:      # independent
                ui_vt = ui.intersection(T_b[node])
                u_vn = u.intersection(T_b[n])
                if ui_vt == u_vn:
                    w = ui.intersection(u)
                    u_list.append(size - len(w))
        if u_list: t_list.append(max(u_list))
    return sum(t_list)

def independent(s, G):
    for n in s:
        k = s - set([n])
        if k.intersection(set(G[n])):
            return False
    return True


def powerset(in_set):
    #print(in_set)
    res = list()
    for z in chain.from_iterable(combinations(in_set,r) for r in range(len(in_set)+1)):
        res.append(frozenset(z))
    return res







if __name__ == '__main__':
    main(sys.argv[1:])
    #print(powerset(set([1,2,3])))
