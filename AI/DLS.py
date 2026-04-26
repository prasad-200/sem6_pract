def dls(graph,node,goal,limit,open_list,visited):
    print("Opened list:",open_list);
    print("Closed list:",visited);
    
    if node not in visited:
        open_list.remove(node);
    
    print("Visited node:",node);
    if node==goal:
        print("Goal Found!");
        return True;

    if limit<=0:
        visited.append(node);
        return False;

    visited.append(node);
    for neighbour in graph[node]:
        if neighbour not in open_list and neighbour not in visited:
            open_list.append(neighbour);


    for neighbour in graph[node]:
        if neighbour not in visited:
            if dls(graph,neighbour,goal,limit-1,open_list,visited):
                return True;

    return False;


graph={};

n=int(input("Enter the number of nodes:"));

for i in range(n):
    node=input("Enter the node:");
    neighbour=input(f"Enter the neighbours of node {node}:").split();
    graph[node]=neighbour;



start=input("Enter the start node:");
goal=input("ENter the goal node:");
limit=int(input("Enter the limit for DLS"));

visited=[];
open_list=[start];
if not dls(graph,start,goal,limit,open_list,visited):
    print("Goal not found in given depth");

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
# ENter the goal node:F
# Enter the limit for DLS1
# Opened list: ['A']
# Closed list: []
# Visited node: A
# Opened list: ['B', 'C']
# Closed list: ['A']
# Visited node: B
# Opened list: ['C']
# Closed list: ['A', 'B']
# Visited node: C
# Goal not found in given depth