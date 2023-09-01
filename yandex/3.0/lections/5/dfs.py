def dfs(graph, visited, curr_edge):
    visited[curr_edge] = True

    for edge in graph[curr_edge]:
        if not visited[edge]:
            dfs(graph, visited, edge)

def get_components(graph):
    visited = [False for i in range(len(graph))]

    n_components = 1

    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, visited, i)
            n_components += 1

    return n_components

if __name__ == "__main__":
    pass