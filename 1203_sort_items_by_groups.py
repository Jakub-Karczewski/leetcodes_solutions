class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        group_copy = copy.deepcopy(group)
        group_copy.sort()
        reindex = dict()
        prev = None
        count = 0
        for i, x in enumerate( group_copy ):
            if x != -1 and x != prev:
                reindex[x] = count
                count += 1
            prev = x

        for i, x in enumerate(group):
            if x != -1:
                group[i] = reindex[group[i]]
        
        prev = count
        act_max_group = count-1
        count_group = [0 for _ in range(prev)]
        indexes_per_group = [[] for _ in range(prev)]
        indexes_ungrouped = dict()

        for i, g in enumerate(group):
            if g != -1:
                count_group[g] += 1
                indexes_per_group[g].append(i)
            else:
                act_max_group += 1
                group[i] = act_max_group
                indexes_ungrouped[group[i]] = i
        
        num_groups = act_max_group + 1

        in_edges = [0 for _ in range(n)]
        graph_per_group = [dict() for _ in range(prev)]

        groups_graph = [set() for _ in range(num_groups)]
        groups_graph_order = []


        for i in range(len(group)):
            before_each = beforeItems[i]
            for x in before_each:
                if group[x] != group[i]:
                    groups_graph[group[x]].add(group[i])
                else:
                    lst = graph_per_group[group[i]].get(x, [])
                    lst.append(i)
                    graph_per_group[group[i]][x] = lst
                    in_edges[i] += 1

            
        def find_cycles_with_dfs(G, idx, vis, w, per_group):
            vis[w] = 1
            if not isinstance(G, dict) or G.get(w, -1) != -1:
                for x in list(G[w]):
                    if not per_group or group[x] == idx:
                        if vis[x] == 0:
                            vis[x] = 1
                            if find_cycles_with_dfs(G, idx, vis, x, per_group):
                                return True
                        elif vis[x] == 1:
                            return True
            vis[w] = 2
            return False


        def top_sort(G, idx, vis, w, per_group):
            vis[w] = 1
            if not isinstance(G, dict) or G.get(w, -1) != -1:
                for x in list(G[w]):
                    if (not per_group or group[x] == idx) and not vis[x]:
                        vis[x] = 1
                        top_sort(G, idx, vis, x, per_group)
            
            if per_group:
                top_order[idx].append(w)
            else:
                groups_graph_order.append(w)
            

        def reset_(tab, idxs):
            if idxs is not None:
                for x in idxs:
                    tab[x] = 0
            else:
                for i in range(len(tab)):
                    tab[i] = 0

        visited = [0 for _ in range(n)]
        top_order = [[] for _ in range(prev)]

        for i in range(prev):

            if count_group[i] > 0 and not any(1 for x in indexes_per_group[i] if in_edges[x] == 0):
                return []

            for ind in indexes_per_group[i]:
                if in_edges[ind] == 0:
                    if(find_cycles_with_dfs(graph_per_group[i], i, visited, ind, True)):
                        return []

            reset_(visited, indexes_per_group[i])

            for ind in indexes_per_group[i]:
                if in_edges[ind] == 0:
                    top_sort(graph_per_group[i], i, visited, ind, True)
            
            reset_(visited, indexes_per_group[i])


        in_edges_global = [0 for _ in range(num_groups)]

        for i in range(num_groups):
            for x in list(groups_graph[i]):
                in_edges_global[x] += 1
        
        for i in range(num_groups):
            if in_edges_global[i] == 0:
                if find_cycles_with_dfs(groups_graph, -2, visited, i, False):
                    return []

        reset_(visited, None)
        for i in range(num_groups):
            if in_edges_global[i] == 0:
                top_sort(groups_graph, -2, visited, i, False)


        sol = []
        print(groups_graph_order)
        for x in groups_graph_order:
            if x >= prev:
                sol.append(indexes_ungrouped[x])
            else:
                sol.extend(top_order[x])
        sol.reverse()
        return sol
