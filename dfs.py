def dfs(graph,root):
    visited=set()
    stack=collections.deque([root])
    visited.add(root)
    while stack:
        r=stack.pop()
        print(r," ",end="")
        for child in graph[r]:
            if child not in visited:
                visited.add(child)
                stack.append(child)
                
graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')
# 0 1 4 3 2
