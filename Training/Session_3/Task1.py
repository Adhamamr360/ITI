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
    (914612, "Emma Watson", 1990)
]

stars = [
    (102, 104257), (102, 112384), (129, 104257), (129, 95953), (144, 93779),
    (158, 109830), (158, 112384), (1597, 93779), (163, 95953), (1697, 93779),
    (193, 104257), (197, 104257), (200, 112384), (398, 109830), (420, 95953),
    (596520, 95953), (641, 109830), (641, 112384), (705, 109830), (705, 93779)
]

# Build the graph
graph = {}

for person_id, movie_id in stars:
    if person_id not in graph:
        graph[person_id] = []
    if movie_id not in graph:
        graph[movie_id] = []
    graph[person_id].append(movie_id)
    graph[movie_id].append(person_id)

visited = []  #List for visited nodes.
queue = []    #Initialize a queue

def bfs(visited, graph, node, goal): #Function for BFS
    visited.append(node)
    queue.append((node, [node]))

    while queue:                #Creating loop to visit each node
        m, path = queue.pop(0)  #Dequeue
        if m == goal:
            return path

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)  #Enqueue
                queue.append((neighbour, path + [neighbour]))

    return None

# Map person ids to names
person_id_to_name = {person_id: name for person_id, name, _ in people}

# Driver Code
source_person = 102  #Kevin Bacon
destination_person = 705  #Robin Wright

path = bfs(visited, graph, source_person, destination_person)

if path:
    print("Path found:")
    for node in path:
        if node in person_id_to_name:
            print(person_id_to_name[node])
        else:
            print(f"Movie ID: {node}")
else:
    print("No path found.")
