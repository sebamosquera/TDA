def searching_algo_BFS(graph, s, t, parent):
    visited = [False] * (graph.m_num_of_nodes)
    queue = []

    queue.append(s)
    visited[s] = True

    while queue:

        u = queue.pop(0)

        for ind, val in enumerate(graph.m_adj_matrix[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False


def ford_fulkerson(graph, source, sink):
    parent = [-1] * (graph.m_num_of_nodes)
    max_flow = 0

    while searching_algo_BFS(graph, source, sink, parent):

        path_flow = float("Inf")
        s = sink
        while (s != source):
            path_flow = min(path_flow, graph.m_adj_matrix[parent[s]][s])
            s = parent[s]

        # Adding the path flows
        max_flow += path_flow

        # Updating the residual values of edges
        v = sink
        while (v != source):
            u = parent[v]
            graph.m_adj_matrix[u][v] -= path_flow
            graph.m_adj_matrix[v][u] += path_flow
            v = parent[v]

    return max_flow
