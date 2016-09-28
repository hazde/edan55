import copy
import time
count = 0
def main():
    lines = open('data/g110.in').read()
    lines = lines.splitlines()
    N = int(lines[0])
    G = dict()
    for i in range(1, N+1):
        vals = lines[i].split()
        G[i-1] = [j for j in range(len(vals)) if int(vals[j])]
    t1 = time.clock()
    print(R_2(G))
    print(str((time.clock() - t1) * 1000) + 'ms')
    print('Total count, |V|: ' + str(count) + ', ' + str(N))
    
def degree_x(G, n):
    for k in G:
        if len(G[k]) == n: return k
    return -1

def R_0(G):
    global count
    count += 1
    if not len(G): return 0
    
    node = degree_x(G, 0)
    if node != -1:
        del G[node]
        return 1 + R_0(G)
    else:
        g4 = copy.deepcopy(G)
        ind = max(G, key= lambda x: len(G[x]))
        l = G[ind]
        del G[ind]
        for k in l:
            del G[k]
        for k1 in G:
            for k2 in l:
                if k2 in G[k1]: G[k1].remove(k2)
        for k3 in g4:
            if ind in g4[k3]: g4[k3].remove(ind)

        del g4[ind]
        return max(1 + R_0(G), R_0(g4))


def R_1(G):
    global count
    count += 1
    #print('count: ' + str(count))
    #print(G)
    if not len(G): return 0
    node1 = degree_x(G, 1)
    if node1 != -1:
        l = G[node1]
        del G[node1]
        del G[l[0]]
        for k1 in G:
            if node1 in G[k1]: G[k1].remove(node1)
            if l[0] in G[k1]: G[k1].remove(l[0])
        
        
        return 1 + R_1(G)
    node = degree_x(G, 0)
    if node != -1:
        del G[node]
        return 1 + R_1(G)
    else:
        g4 = copy.deepcopy(G)
        ind = max(G, key= lambda x: len(G[x]))
        l = G[ind]
        del G[ind]
        for k in l:
            del G[k]
        for k1 in G:
            for k2 in l:
                if k2 in G[k1]: G[k1].remove(k2)
        for k3 in g4:
            if ind in g4[k3]: g4[k3].remove(ind)

        del g4[ind]
        return max(1 + R_1(G), R_1(g4))

def neighbors(G, u, w):
    return w in G[u]

def R_2(G):
    global count
    count += 1
    #print('count: ' + str(count))
    #print(G)
    if not len(G): return 0
    n2 = degree_x(G, 2)
    if n2 != -1:
        l = G[n2]
        if neighbors(G, l[0], l[1]):
            del G[n2], G[l[0]], G[l[1]]
            for k in G:
                if l[0] in G[k]: G[k].remove(l[0])
                if l[1] in G[k]: G[k].remove(l[1])
                if n2 in G[k]: G[k].remove(n2)
            return 1 + R_2(G)
        else:
            l1 = G[l[0]] + list(set(G[l[1]]) - set(G[l[0]]))
            l1.remove(n2)
            new = max(G.keys(), key=int)+1 
            G[new] = l1
            for k in l1:
                G[k].append(new)
            del G[n2], G[l[0]], G[l[1]]
            for k in G:
                if l[0] in G[k]: G[k].remove(l[0])
                if l[1] in G[k]: G[k].remove(l[1])
                if n2 in G[k]: G[k].remove(n2)
            return 1 + R_2(G)
            
    node1 = degree_x(G, 1)
    if node1 != -1:
        l = G[node1]
        del G[node1]
        del G[l[0]]
        for k1 in G:
            if node1 in G[k1]: G[k1].remove(node1)
            if l[0] in G[k1]: G[k1].remove(l[0])
        
        
        return 1 + R_2(G)
    node = degree_x(G, 0)
    if node != -1:
        del G[node]
        return 1 + R_2(G)
    else:
        g4 = copy.deepcopy(G)
        ind = max(G, key= lambda x: len(G[x]))
        l = G[ind]
        del G[ind]
        for k in l:
            del G[k]
        for k1 in G:
            for k2 in l:
                if k2 in G[k1]: G[k1].remove(k2)
        for k3 in g4:
            if ind in g4[k3]: g4[k3].remove(ind)

        del g4[ind]
        return max(1 + R_2(G), R_2(g4))

if __name__ == '__main__':
    main()

