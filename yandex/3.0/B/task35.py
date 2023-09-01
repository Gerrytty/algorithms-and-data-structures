def create_connectivity(connectivity_matrix):

    v = len(connectivity_matrix)

    arr = [[] for i in range(v)]
    colors = [0 for i in range(v)]

    for i in range(v):
        for j in range(v):
            if matrix[i][j] == 1:
                arr[i].append(j)

    return arr, colors

have_loop = False

path = []

def dfs(graph, visited, colors, curr_edge, from_edge, path, connectivity_matrix):

    visited[curr_edge] = True
    colors[curr_edge] = 1

    path.append(curr_edge)

    for edge in graph[curr_edge]:

        if edge == from_edge:
            continue

        if not visited[edge]:
            cycle = dfs(graph, visited, colors, edge, curr_edge, path, connectivity_matrix)

            if cycle is not None:
                return cycle

        if colors[edge] == 1:
            global have_loop
            have_loop = True
            path = path[path.index(edge):]
            return path[path.index(edge):]

    # цикл по соседям закончился
    colors[curr_edge] = 2
    path.pop(-1)
    return None

def process_all_graph(graph, visited, colors):
    comp = 1
    some_loop = False
    for i in range(0, len(graph)):
        if not visited[i]:
            out = dfs(graph, visited, colors, i, i, path, None)

            if have_loop:
                print("YES")
                print(len(out))
                a = []
                for p in out:
                    a.append(p + 1)
                print(*a[::-1])
                # print(*out)
                some_loop = True
                break
            comp += 1

    if not some_loop:
        print("NO")

# 3
# 0 1 1
# 1 0 0
# 1 0 0

if __name__ == "__main__":
    matrix_size = int(input())

    matrix = []

    for i in range(matrix_size):
        matrix.append(list(map(int, input().split())))

    arr, colors = create_connectivity(matrix)

    visited = [False for i in range(matrix_size)]

    out_path = []

    # colors[0] = 0
    # dfs(arr, visited, colors, 0, 0, out_path, matrix)

    process_all_graph(arr, visited, colors)
