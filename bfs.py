import collections
def bfS(graph,root):
    visited=set()
    queue=collections.deque([root])
    visited.add(root)
    while queue:
        r=queue.popleft()
        print(r,"--",end="")
        for child in graph[r]:
            if child not in visited:
                visited.add(child)
                queue.append(child)
                
graph={
    'a':['b','c'],
    'b':['c','e','f'],
    'e':['f','b'],
    'f':['b','c','g'],
    'g':['f','g'],
    'c':['a','b','d','f'],
    'd':['c','g']
}

bfS(graph,root='a')
# a--b--c--e--f--d--g 
