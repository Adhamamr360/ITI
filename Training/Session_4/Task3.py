import matplotlib.pyplot as plt  # (1) pip install matplotlib
import networkx as nx  #(2) pip install networkx

movies = [
    (112384, "Apollo 13", 1995),
    (104257, "A Few Good Men", 1992),
    (109830, "Forrest Gump", 1994),
    (93779, "The Princess Bride", 1987),
    (95953, "Rain Man", 1988)
]

people = [
    (102, "Kevin Bacon", 1958),
    (129, "Tom Cruise", 1962),
    (144, "Cary Elwes", 1962),
    (158, "Tom Hanks", 1956),
    (1597, "Mandy Patinkin", 1952),
    (163, "Dustin Hoffman", 1937),
    (1697, "Chris Sarandon", 1942),
    (193, "Demi Moore", 1962),
    (197, "Jack Nicholson", 1937),
    (200, "Bill Paxton", 1955),
    (398, "Sally Field", 1946),
    (420, "Valeria Golino", 1965),
    (596520, "Gerald R. Molen", 1935),
    (641, "Gary Sinise", 1955),
    (705, "Robin Wright", 1966),
]

stars = [
    (102, 104257), (102, 112384), (129, 104257), (129, 95953), (144, 93779),
    (158, 109830), (158, 112384), (1597, 93779), (163, 95953), (1697, 93779),
    (193, 104257), (197, 104257), (200, 112384), (398, 109830), (420, 95953),
    (596520, 95953), (641, 109830), (641, 112384), (705, 109830), (705, 93779)
]

# Build the graph
G = nx.Graph()
labels = {}

for person_id, name, _ in people:
    G.add_node(person_id)
    labels[person_id] = name

for movie_id, title, _ in movies:
    G.add_node(movie_id)
    labels[movie_id] = title

for person_id, movie_id in stars:
    G.add_edge(person_id, movie_id)

visited = []  # List for visited nodes.
queue = []    # Initialize a queue

def bfs(visited, graph, node, goal): # Function for BFS
    visited.append(node)
    queue.append((node, [node]))

    while queue:                # Creating loop to visit each node
        m, path = queue.pop(0)  # Dequeue
        if m == goal:
            return path

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)  # Enqueue
                queue.append((neighbour, path + [neighbour]))

    return None

# Map person ids to names
person_id_to_name = {person_id: name for person_id, name, _ in people}

# Driver Code
source_person = 102  # Kevin Bacon
destination_person = 705  # Robin Wright

path = bfs(visited, G, source_person, destination_person)

if path:
    print("Path found:")
    for node in path:
        if node in person_id_to_name:
            print(person_id_to_name[node])
        else:
            print(f"Movie ID: {node}")
else:
    print("No path found.")

# Visualize the graph
pos = nx.spring_layout(G)

plt.figure(figsize=(15, 10))

# person nodes
person_nodes = [person_id for person_id, name, _ in people]
nx.draw_networkx_nodes(G, pos, nodelist=person_nodes, node_size=500, node_color='lightblue')

# movie nodes
movie_nodes = [movie_id for movie_id, title, _ in movies]
nx.draw_networkx_nodes(G, pos, nodelist=movie_nodes, node_size=500, node_color='lightgreen')

# Draw edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# Draw labels
nx.draw_networkx_labels(G, pos, labels, font_size=8)

# Highlight the path found
if path:
    path_edges = [(path[n], path[n+1]) for n in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2.5, edge_color='r')

plt.title('Six Degrees of Kevin Bacon')
plt.show()
