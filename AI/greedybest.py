def greedy(graph,start,goal,heu):
    open_list=[start];
    visited=[];
    
    while open_list:
        print("\nOPENED LIST:",open_list)
        print("CLOSED LIST:",visited);
         
        open_list.sort(key=lambda x: heu[x]);
        node = open_list.pop(0);

        if node not in visited:
            print("Visited node:",node);
            visited.append(node);

            if goal == node:
                print("Goal node Found!");
                return;

            for neighbour in graph[node]:
                if neighbour not in visited and neighbour not in open_list:
                    open_list.append(neighbour);

    print("Goal node not found!");


graph={};
n=int(input("Enter the number of nodes:"));

for i in range(n):
    node=input("Enter the node:");
    neighbour=input(f"Enter the neighbours of node {node}:").split();
    graph[node]=neighbour;

heu={};
print("Enter the heuristic value of nodes:");

for nodes in graph:
    h=int(input(f"h({nodes}) :"));
    heu[nodes]=h;

start=input("Enter the start node:");
goal=input("Enter the goal node:");

greedy(graph,start,goal,heu);


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
# Enter the heuristic value of nodes:
# h(A) :5
# h(B) :4
# h(C) :3
# h(D) :2
# h(E) :6
# h(F) :0
# Enter the start node:A
# Enter the goal node:F
# /nOPENED LIST: ['A']
# CLOSED LIST: []
# Visited node: A
# /nOPENED LIST: ['B', 'C']
# CLOSED LIST: ['A']
# Visited node: C
# /nOPENED LIST: ['B', 'F']
# CLOSED LIST: ['A', 'C']
# Visited node: F
# Goal node Found!