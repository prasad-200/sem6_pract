def bfs(graph,start,goal):
    queue=[start];
    visited=[];

    while queue:
        print("Opened list :",queue);
        print("Closed List :",visited);
        
        node=queue.pop(0);

        if node not in visited:
            print("Visited node:",node);
            visited.append(node);

            if node==goal:
                print(queue);
                print(visited);
                print("Goal node found!")
                return;

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour);

    print("Goal node not Found:");        


graph={};

n=int(input("Enter the number of nodes:"));

for i in range(n):
    node=input("Enter the node:");
    neighbours=input(f"Enter the neighbbours of node {node}:").split();
    graph[node]=neighbours;

start=input("Enter the start node:");
goal=input("Enter the goal node:");

bfs(graph,start,goal);


# Enter the number of nodes:6
# Enter the node:A
# Enter the neighbbours of node A:B C
# Enter the node:B
# Enter the neighbbours of node B:D E
# Enter the node:C
# Enter the neighbbours of node C:F
# Enter the node:D
# Enter the neighbbours of node D:
# Enter the node:E
# Enter the neighbbours of node E:
# Enter the node:F
# Enter the neighbbours of node F:
# Enter the start node:A
# Enter the goal node:F
# ['A']
# []
# Visited node: A
# ['B', 'C']
# ['A']
# Visited node: B
# ['C', 'D', 'E']
# ['A', 'B']
# Visited node: C
# ['D', 'E', 'F']
# ['A', 'B', 'C']
# Visited node: D
# ['E', 'F']
# ['A', 'B', 'C', 'D']
# Visited node: E
# ['F']
# ['A', 'B', 'C', 'D', 'E']
# Visited node: F
# []
# ['A', 'B', 'C', 'D', 'E', 'F']
# Goal node found!