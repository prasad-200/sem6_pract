def astar(graph,start,goal,heu,cost):
    open=[start];
    closed=[];

    g={start:0};
    parent={start:None};

    while open:
        open.sort(key=lambda x : g[x]+heu[x]);

        print("Open list:",open);
        print("Closed list:",closed);

        node = open.pop(0);

        if node ==goal:
            print("Goal node found!");
            print_path(parent,goal);
            return;

        closed.append(node);

        for neighbour,c in cost[node]:

            new_g=g[node]+c;

            if neighbour not in g or new_g<g[neighbour]:
                g[neighbour]=new_g;
                parent[neighbour]=node;

                if neighbour not in open and neighbour not in closed:
                    open.append(neighbour);

    print("Goal not found");


def print_path(parent,goal):
    path=[];

    while goal is not None:
        path.append(goal);
        goal=parent[goal];

    path.reverse();
    print("Path:","->".join(path));


graph={};
cost={};

n=int(input("Enter the number of node:"));

for i in range(n):
    node=input("Enter the node:");
    neighbour=input(f"Enter the neighbours of node {node}:").split();
    graph[node]=neighbour;
    cost[node]=[];

    for nb in neighbour:
        c=int(input(f"Enter the cost from {node} to {nb}"));
        cost[node].append((nb,c));

heu={};
for node in graph:
    h=int(input(f"Enter the heuristic value of node {node}"));
    heu[node]=h;

start=input("Enter the start node:");
goal=input("Enter the goal node:");

astar(graph,start,goal,heu,cost);

# Enter the number of node:6
# Enter the node:A
# Enter the neighbours of node A:B C
# Enter the cost from A to B1
# Enter the cost from A to C4
# Enter the node:B
# Enter the neighbours of node B:D E
# Enter the cost from B to D2
# Enter the cost from B to E5
# Enter the node:C
# Enter the neighbours of node C:F
# Enter the cost from C to F1
# Enter the node:D
# Enter the neighbours of node D:
# Enter the node:E
# Enter the neighbours of node E:
# Enter the node:F
# Enter the neighbours of node F:
# Enter the heuristic value of node A5
# Enter the heuristic value of node B4
# Enter the heuristic value of node C2
# Enter the heuristic value of node D6
# Enter the heuristic value of node E3
# Enter the heuristic value of node F0
# Enter the start node:A
# Enter the goal node:F
# Open list: ['A']
# Closed list: []
# Open list: ['B', 'C']
# Closed list: ['A']
# Open list: ['C', 'D', 'E']
# Closed list: ['A', 'B']
# Open list: ['F', 'D', 'E']
# Closed list: ['A', 'B', 'C']
# Goal node found!
# Path: A->C->F
