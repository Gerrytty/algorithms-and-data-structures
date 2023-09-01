def read_and_create(n):

	graph = {}

	for i in range(n):
		line = list(map(int, input().split()))

		for j in range(len(line)):

			if line[j] == 1:

				if i in graph:
					graph[i].append(j)
				else:
					graph[i] = [j]

	return graph

def bfs(graph, n, start, end):

	queue = [start]

	visited = [0 for i in range(n)]
	paths = [0 for i in range(n)]
	prevs = [-1 for i in range(n)]

	if start == end:
		return 0, []

	while len(queue) > 0:
		vertex = queue.pop(0)

		if visited[vertex] == 1:
			continue

		if end in graph[vertex]:
			paths[end] = paths[vertex] + 1
			prevs[end] = vertex
			out = []
			curr = end
			for i in range(paths[end] + 1):
				out.append(curr)
				curr = prevs[curr]
			return paths[end], out[::-1]

		for v in graph[vertex]:
			if visited[v] == 0 and prevs[v] == -1:
				queue.append(v)
				paths[v] = paths[vertex] + 1
				prevs[v] = vertex

		visited[vertex] = 1


	return -1, []

n = int(input())

g = read_and_create(n)

start, end = map(int, input().split())

if start-1 in g and end-1 in g:

	path = bfs(g, n, start-1, end-1)

	print(path[0])

	if len(path[1]) > 0:
		print(*path[1][::-1])

else:
	print(-1)