class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Complexity of my solution is O(E * V * log(E)) 
        # According to some sources, probably there exists a solution that is O(E log E) or O(E * V), TODO
        
        class UnionFind:
            def __init__(self,n):
                self.root = [i for i in range(n)]
                self.rank = [1 for i in range(n)]

            def find(self,x):
                if self.root[x] == x:
                    return x
                self.root[x] = self.find(self.root[x])
                return self.root[x]
            def union(self,x,y):
                rootX,rootY = self.find(x),self.find(y)
                if rootX!=rootY:
                    if self.rank[rootX]>self.rank[rootY]:
                        self.root[rootY] = rootX
                    elif self.rank[rootX]<self.rank[rootY]:
                        self.root[rootX] = rootY
                    else:
                        self.root[rootY] = rootX
                        self.rank[rootX] +=1
        def Kruskal(edges,n,ignored,first = False):
            weight = 0
            uf = UnionFind(n)
            ans = []
            for i in range(len(edges)):
                u,v,w,j = edges[i][0],edges[i][1],edges[i][2],edges[i][3]
                if i == ignored:
                    continue
                if uf.find(u) != uf.find(v):
                    if first:
                        in_mst[i] = True
                    ans.append([u,v,w,i,j])
                    uf.union(u,v)
                    weight+=w
            return weight,ans,uf
        for i in range(len(edges)):
            edges[i].append(i) 
            # We need to keep track of indexes before sorting
        edges.sort(key = lambda x: x[2])
        visited = [False for _ in range(len(edges))]
        in_mst = [False for _ in range(len(edges))]
        weight,mst_edges,mst_uf = Kruskal(edges,n,-1,True)
        ans = [[],[]]
        for j,e in enumerate(mst_edges):
            idx = e[3]
            new_weight,new_edges,new_uf = Kruskal(mst_edges,n,j)
            flag = False

            for i in range(idx-1,-1,-1):
                if edges[i][2] < e[2]:
                    break
                else:
                    if not in_mst[i]:
                        if new_uf.find(edges[i][0]) != new_uf.find(edges[i][1]):
                            
                            if not visited[i]:
                                ans[1].append(edges[i][3])
                                visited[i] = True
                            flag = True
                        
                
            for i in range(idx+1,len(edges)):
                if edges[i][2] > e[2]:
                    break
                else:
                    if not in_mst[i]:
                        if new_uf.find(edges[i][0]) != new_uf.find(edges[i][1]):
                            
                            if not visited[i]:
                                ans[1].append(edges[i][3])
                                visited[i] = True
                            flag = True
                        
            if flag:
                ans[1].append(e[4])
            else:
                ans[0].append(e[4])
        return ans
