def dfs(graph,start,goal):
    stack=[start];
    visited=[];

    while stack:
        print("open list:",stack);
        print("Closed list:",visited);
        node=stack.pop();

        if node not in visited:
            visited.append(node);
            print("Visited node:",node)

            if node==goal:
                print("Goal Found!");
                return 
            
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour);
    
    print("Goal not found!");



graph={};
n=int(input("Enter the number of nodes:"));

for i in range (n):
    node=input("Enter the node:");
    neighbours=input(f"Enter the neighbours of node {node}:").split();
    graph[node]=neighbours;


start=input("Enter the start node:");
goal=input("Enter the goal node:");

dfs(graph,start,goal);


# output:
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
# opee list: ['A']
# Closed list: []
# Visited node: A
# opee list: ['C', 'B']
# Closed list: ['A']
# Visited node: B
# opee list: ['C', 'E', 'D']
# Closed list: ['A', 'B']
# Visited node: D
# opee list: ['C', 'E']
# Closed list: ['A', 'B', 'D']
# Visited node: E
# opee list: ['C']
# Closed list: ['A', 'B', 'D', 'E']
# Visited node: C
# opee list: ['F']
# Closed list: ['A', 'B', 'D', 'E', 'C']
# Visited node: F
# Goal Found!


