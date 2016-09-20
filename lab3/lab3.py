import copy
count = 0
def main():
    lines = open('data/g70.in').read()
    lines = lines.splitlines()
    N = int(lines[0])
    G = dict()
    for i in range(1, N+1):
        vals = lines[i].split()
        G[i-1] = [j for j in range(len(vals)) if int(vals[j])]
  
    print(R_0(G))    
    print(count)
    

def find_empty(G):
    for k in G:
        if not len(G[k]): return k
    return -1


def R_0(G):
    global count
    count += 1
    if not len(G): return 0
    node = find_empty(G)
    if node != -1:
        g2 = copy.deepcopy(G)
        l = g2[node]
        for k in l:
            g2[k].remove(node)
        del g2[node]
        return 1 + R_0(g2)
    else:
        g3 = copy.deepcopy(G)
        g4 = copy.deepcopy(G)
        ind = max(G, key= lambda x: len(G[x]))
        l = G[ind]
        del g3[ind]
        for k in l:
            del g3[k]
        for k1 in g3:
            for k2 in l:
                if k2 in g3[k1]: g3[k1].remove(k2)
        for k3 in g4:
            if ind in g4[k3]: g4[k3].remove(ind)

        del g4[ind]
        return max(1 + R_0(g3), R_0(g4))

if __name__ == '__main__':
    main()

