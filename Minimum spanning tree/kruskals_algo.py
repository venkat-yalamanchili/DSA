class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(0,n+1)]
        self.rank = [0] * (n+1)


    def find(self,x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True

def kruskals_mst(V, edges):
    edges.sort(key=lambda x: x[2])

    dsu = DisjointSet(V)
    mst_weight = 0

    for u,v,wt in edges:
        if dsu.union(u,v):  #or if dsu.find(u) != dsu.find(v):
            print(u,v,wt)
            mst_weight+= wt
    return mst_weight

if __name__ == '__main__':
    
    # An edge contains, weight, source and destination
    edges = [[0, 1, 10], [1, 3, 15], [2, 3, 4], [2, 0, 6], [0, 3, 5]]
    print(kruskals_mst(4, edges))