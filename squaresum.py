#  ┌─────────────────────────────────────────────────────────┐
#  │  File name: squaresum.py                                │
#  │  Author: David De Potter, pl3onasm@gmail.com            │
#  │  License: refer to the license file in this repository  │
#  │  Description: computes a path in which the sum of any   │
#  │  two adjacent vertices yields a perfect square          │
#  └─────────────────────────────────────────────────────────┘

import sys
from math import ceil, sqrt
from collections import defaultdict

sys.setrecursionlimit(250000)

def dfs (graph, vertices, path, n):
  if len(path) == n:
    yield path
  vertices.sort(key=lambda k: len(graph[k]))

  for vertex in vertices:
    path += [vertex]
    for val in graph[vertex]:
      graph[val].remove(vertex)
    yield from dfs(graph, graph[vertex], path, n)
    path.pop()
    for val in graph[vertex]:
      graph[val] += [vertex]

def squareSum(n):
  graph = defaultdict(list)
  lim = ceil(sqrt(2*n))
  squares = {s**2 for s in range(2,lim)}
  vertices = [v for v in range(1,n+1)]

  for vertex in vertices:
    for adjacent in vertices[vertex:]:
      if adjacent + vertex in squares:
        graph[vertex] += [adjacent]
        graph[adjacent] += [vertex]

  return next(dfs(graph, vertices, [], n), None)

if __name__ == "__main__":
  print(squareSum(int(sys.argv[1]))) 
  
    