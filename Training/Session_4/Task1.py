from queue import PriorityQueue
import timeit

class MazeState:
    def __init__(self, position, parent=None, g=0, heuristic=0):
        self.position = position
        self.parent = parent
        self.g = g  # Cost to reach the current node (for A*)
        self.heuristic = heuristic  # Estimated cost to reach the goal (h)

    def f(self):
        return self.g + self.heuristic  # Total cost function f = g + h

    def __lt__(self, other):
        return self.f() < other.f()

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

def misplaced_tiles(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def generate_neighbors(state, maze, goal, heuristic_func, is_a_star):
    neighbors = []
    x, y = state.position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '0':
            if is_a_star:
                g = state.g + 1  # Cost to reach the neighbor (only for A*)
                heuristic = heuristic_func((new_x, new_y), goal)
                neighbors.append(MazeState((new_x, new_y), state, g, heuristic))
            else:
                heuristic = heuristic_func((new_x, new_y), goal)
                neighbors.append(MazeState((new_x, new_y), state, heuristic=heuristic))
    return neighbors

def a_star_search(maze, start, goal, heuristic_func):
    boardQueue = PriorityQueue()
    start_state = MazeState(start, g=0, heuristic=heuristic_func(start, goal))
    boardQueue.put(start_state)
    boardVisited = set()
    visited_tiles = set()

    while not boardQueue.empty():
        current_state = boardQueue.get()
        visited_tiles.add(current_state.position)

        if current_state.position == goal:
            return reconstruct_path(current_state), len(visited_tiles)

        boardVisited.add(current_state)

        for neighbor in generate_neighbors(current_state, maze, goal, heuristic_func, is_a_star=True):
            if neighbor not in boardVisited and all(not (node == neighbor and node.f() <= neighbor.f()) for node in boardQueue.queue):
                boardQueue.put(neighbor)

    return None, len(visited_tiles)

def greedy_best_first_search(maze, start, goal, heuristic_func):
    boardQueue = PriorityQueue()
    start_state = MazeState(start, heuristic=heuristic_func(start, goal))
    boardQueue.put(start_state)
    boardVisited = set()
    visited_tiles = set()
    
    while not boardQueue.empty():
        current_state = boardQueue.get()
        visited_tiles.add(current_state.position)
        
        if current_state.position == goal:
            return reconstruct_path(current_state), len(visited_tiles)
        
        boardVisited.add(current_state)
        
        for neighbor in generate_neighbors(current_state, maze, goal, heuristic_func, is_a_star=False):
            if neighbor not in boardVisited:
                boardQueue.put(neighbor)
    
    return None, len(visited_tiles)

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.position)
        state = state.parent
    return path[::-1]

def find_positions(maze):
    start = None
    goal = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'A':
                start = (i, j)
            elif maze[i][j] == 'B':
                goal = (i, j)
    return start, goal

maze = [
    "01111111111B",
    "010000000001",
    "010111111101",
    "010100000101",
    "011101111101",
    "000101000001",
    "A11101111111"
]

maze = [list(row) for row in maze]
start, goal = find_positions(maze)

# A* with Misplaced Tiles
print("A* with Misplaced Tiles")
def a_star_task():
    path, num_visited_tiles = a_star_search(maze, start, goal, misplaced_tiles)
    return num_visited_tiles

time_taken = timeit.timeit(a_star_task, number=1)
path, num_visited_tiles = a_star_search(maze, start, goal, misplaced_tiles)  # Run again to get path
if path:
    print(f"Path found with A*")
else:
    print("No solution found.")
print(f"Number of tiles visited: {num_visited_tiles}")
print(f"Time taken: {time_taken:.6f} seconds\n")

# Greedy Best-First Search with Misplaced Tiles
print("Greedy Best-First Search with Misplaced Tiles")
def greedy_task():
    path, num_visited_tiles = greedy_best_first_search(maze, start, goal, misplaced_tiles)
    return num_visited_tiles

time_taken = timeit.timeit(greedy_task, number=1)
path, num_visited_tiles = greedy_best_first_search(maze, start, goal, misplaced_tiles)  # Run again to get path
if path:
    print(f"Path found with Greedy")
else:
    print("No solution found.")
print(f"Number of tiles visited: {num_visited_tiles}")
print(f"Time taken: {time_taken:.6f} seconds\n")
