import random

class VacuumAgent:
    def __init__(self, environment):
        self.environment = environment
        self.position = (0, 0)  # Starting position at (0, 0)
        self.visited_positions = set()
    def __str__(self) -> str:
        return f"The environment of the vacuum agent is {self.environment}, position: {self.position}"

    def model_thinking_movement(self):
        # Define possible movements: (dx, dy)
        directions = {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }

        for direction, (dx, dy) in directions.items():
            new_position = (self.position[0] + dx, self.position[1] + dy)
            if self.is_valid_position(new_position) and new_position not in self.visited_positions:
                if self.environment.is_dirty(new_position):
                    self.position = new_position
                    self.environment.clean(new_position)
                    print(f"Agent moved {direction} and cleaned dirt at position {new_position}")
                    self.visited_positions.add(new_position)
                    return

        # If no dirty adjacent cell is found, choose a random position
        while True:
            new_position = (random.randint(0, self.environment.width - 1), random.randint(0, self.environment.height - 1))
            if new_position not in self.visited_positions:
                self.position = new_position
                print(f"Agent moved randomly to position {new_position}")
                break

    def is_valid_position(self, position):
        x, y = position
        return 0 <= x < self.environment.width and 0 <= y < self.environment.height

    def run(self, steps=100):
        for _ in range(steps):
            print(f"Agent is at position {self.position}")
            self.model_thinking_movement()
            self.environment.print_grid(self.position)
            print()  # Add a blank line between iterations

            # If all states are clean, stop the process
            if self.is_environment_clean():
                print("Environment is clean. Stopping.")
                break

    def is_environment_clean(self):
        for row in self.environment.grid:
            if any(row):
                return False
        return True

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[False for _ in range(width)] for _ in range(height)]  # Initialize grid with no dirt

    def add_dirt(self, position):
        self.grid[position[1]][position[0]] = True

    def clean(self, position):
        self.grid[position[1]][position[0]] = False

    def is_dirty(self, position):
        return self.grid[position[1]][position[0]]
    
    def print_grid(self, agent_position):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (x, y) == agent_position:
                    row += "A  "  # Agent's position
                elif self.grid[y][x]:
                    row += "True  "  # Dirty cell
                else:
                    row += "False "  # Clean cell
            print(row)

# Example usage:
env = Environment(width=5, height=5)
env.add_dirt((1, 1))
env.add_dirt((2, 3))
agent = VacuumAgent(environment=env)
agent.run(steps=100)
