import sys
sys.setrecursionlimit(50000)


def form_connectivity_list(v, e):
    connectivity_list = [[] for i in range(v + 1)]

    for i in range(e):
        v1, v2 = map(int, input().split())
        connectivity_list[v1].append(v2)
        connectivity_list[v2].append(v1)

    return connectivity_list

def dfs(graph, visited, curr_edge, comp, list_of_components):
    visited[curr_edge] = True
    list_of_components[curr_edge] = comp

    for edge in graph[curr_edge]:
        if not visited[edge]:
            dfs(graph, visited, edge, comp, list_of_components)

def get_n_comp(graph, visited):

    comp_list = [-1 for i in range(v + 1)]

    comp = 1
    for i in range(1, len(graph)):
        if not visited[i]:
            dfs(graph, visited, i, comp, comp_list)
            comp += 1

    print(comp - 1)

    out = [[] for i in range(comp)]

    for i in range(1, len(comp_list)):
        out[comp_list[i]].append(i)

    for c in out:
        if len(c) != 0:
            print(len(c))
            print(*c)

if __name__ == "__main__":
    v, e = map(int, input().split())
    conn_list = form_connectivity_list(v, e)

    visited = [False for i in range(v + 1)]

    get_n_comp(conn_list, visited)