import heapq
import sys
from PIL import Image, ImageDraw

class Node():
    def __init__(self, state, parent, action, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Maze():

    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def misplaced_tiles(self, state):
        """Calculate the heuristic for the number of misplaced tiles."""
        row, col = state
        goal_row, goal_col = self.goal
        return abs(row - goal_row) + abs(col - goal_col)

    def a_star_solve(self):
        """Finds a solution to maze using A* algorithm."""
        import heapq

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier with the starting position
        start = Node(state=self.start, parent=None, action=None, cost=0, heuristic=self.misplaced_tiles(self.start))
        frontier = []
        heapq.heappush(frontier, (start.cost + start.heuristic, start))

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping until solution found
        while frontier:
            _, node = heapq.heappop(frontier)
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if state not in self.explored:
                    cost = node.cost + 1
                    heuristic = self.misplaced_tiles(state)
                    child = Node(state=state, parent=node, action=action, cost=cost, heuristic=heuristic)
                    heapq.heappush(frontier, (cost + heuristic, child))

    def greedy_best_first_search(self):
        """Finds a solution to maze using Greedy Best-First Search algorithm."""
        import heapq

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier with the starting position
        start = Node(state=self.start, parent=None, action=None, heuristic=self.misplaced_tiles(self.start))
        frontier = []
        heapq.heappush(frontier, (start.heuristic, start))

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping until solution found
        while frontier:
            _, node = heapq.heappop(frontier)
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if state not in self.explored:
                    heuristic = self.misplaced_tiles(state)
                    child = Node(state=state, parent=node, action=action, heuristic=heuristic)
                    heapq.heappush(frontier, (heuristic, child))

    def output_image(self, filename, show_solution=True, show_explored=False):
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        img.save(filename)

# Load the maze
m = Maze("maze.txt")

# Test A* algorithm
print("Solving with A*...")
m.a_star_solve()
print("A* States Explored:", m.num_explored)
print("A* Solution:")
m.print()
m.output_image("maze_a_star.png", show_explored=True)

# Load the maze again
m = Maze("maze.txt")

# Test Greedy Best-First Search algorithm
print("Solving with Greedy Best-First Search...")
m.greedy_best_first_search()
print("Greedy Best-First Search States Explored:", m.num_explored)
print("Greedy Best-First Search Solution:")
m.print()
m.output_image("maze_greedy.png", show_explored=True)
