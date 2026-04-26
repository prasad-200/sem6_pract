def dls(graph,node,goal,limit,visited):
    print("Visited node:",node);

    if node == goal:
        return True;

    if limit<=0:
        return False;

    visited.append(node);

    for neighbour in graph[node]:
        if neighbour not in visited:
            if dls(graph,neighbour,goal,limit-1,visited):
                return True;

    return False;

def dfid(graph,start,goal,max_depth):
    for depth in range(max_depth+1):
        print("For depth:",depth);
        visited=[];

        if dls(graph,start,goal,depth,visited):
            print("Goal node Found at depth ",depth);
            return
        
    print("Goal node not found at given max depth!");


n=int(input("Enter the number of nodes:"));

graph={};

for i in range(n):
    node=input("Enter the node:");
    neighbours=input(f"Enter the neighbours of node {node}:").split();
    graph[node]=neighbours;

start=input("Enter the start node:");
goal=input("Enter the goal node:");
max_depth=int(input("Enter the maximum depth:"));

dfid(graph,start,goal,max_depth);


# Enter the number of nodes:6
# Enter the node:A
# Enter the neighbours of node A:B C
# Enter the node:B
# Enter the neighbours of node B:D E
# Enter the node:C
# Enter the neighbours of node C:F
# Enter the node:D
# Enter the neighbours of node D:
# Enter the node:E
# Enter the neighbours of node E:
# Enter the node:F
# Enter the neighbours of node F:
# Enter the start node:A
# Enter the goal node:F
# Enter the maximum depth:2
# For depth: 0
# Visited node: A
# For depth: 1
# Visited node: A
# Visited node: B
# Visited node: C
# For depth: 2
# Visited node: A
# Visited node: B
# Visited node: D
# Visited node: E
# Visited node: C
# Visited node: F
# Goal node Found at depth  2