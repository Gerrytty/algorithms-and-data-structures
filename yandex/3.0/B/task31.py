import sys
sys.setrecursionlimit(2000)

def form_connectivity_list(v, e):
    connectivity_list = [[] for i in range(v + 1)]

    for i in range(e):
        v1, v2 = map(int, input().split())
        connectivity_list[v1].append(v2)
        connectivity_list[v2].append(v1)

    return connectivity_list

def dfs(graph, visited, curr_edge):
    visited[curr_edge] = True

    for edge in graph[curr_edge]:
        if not visited[edge]:
            dfs(graph, visited, edge)

if __name__ == "__main__":
    v, e = map(int, input().split())
    conn_list = form_connectivity_list(v, e)

    visited = [False for i in range(v + 1)]

    dfs(conn_list, visited, 1)

    out = []

    for i, v in enumerate(visited):
        if v:
            out.append(i)

    print(len(out))
    print(*out)