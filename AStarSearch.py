import heapq

class Node:
    def __init__(self, position, g=0, h=0):
        self.position = position
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic cost from current node to goal
        self.f = g + h  # Total cost
        self.parent = None  # To keep track of the path

    def __lt__(self, other):
        return self.f < other.f

class AStar:
    def __init__(self, start, goal, grid):
        self.start = start
        self.goal = goal
        self.grid = grid
        self.open_list = []
        self.closed_list = set()
        heapq.heappush(self.open_list, Node(start, 0, self.heuristic(start, goal)))
        
    def heuristic(self, current, goal):
        # Use Manhattan distance as heuristic (for a grid with 4 possible moves)
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def get_neighbors(self, node):
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4 possible directions (right, down, left, up)
        for direction in directions:
            neighbor_pos = (node.position[0] + direction[0], node.position[1] + direction[1])
            if 0 <= neighbor_pos[0] < len(self.grid) and 0 <= neighbor_pos[1] < len(self.grid[0]) and self.grid[neighbor_pos[0]][neighbor_pos[1]] == 0:
                neighbors.append(Node(neighbor_pos))
        return neighbors

    def search(self):
        while self.open_list:
            current_node = heapq.heappop(self.open_list)
            self.closed_list.add(current_node.position)
            
            # Check if we have reached the goal
            if current_node.position == self.goal:
                return self.reconstruct_path(current_node)
            
            # Get neighbors
            neighbors = self.get_neighbors(current_node)
            for neighbor in neighbors:
                if neighbor.position in self.closed_list:
                    continue
                
                tentative_g = current_node.g + 1  # Assume cost between adjacent nodes is 1

                if (neighbor.f, neighbor.position) in [(node.f, node.position) for node in self.open_list]:
                    if tentative_g >= neighbor.g:
                        continue

                neighbor.g = tentative_g
                neighbor.h = self.heuristic(neighbor.position, self.goal)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current_node
                
                heapq.heappush(self.open_list, neighbor)

        return None  # No path found

    def reconstruct_path(self, node):
        path = []
        while node:
            path.append((node.position, node.f))
            node = node.parent
        path.reverse()
        return path

# Example usage:
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

astar = AStar(start, goal, grid)
path = astar.search()

if path:
    print("Path found:")
    for position, f_value in path:
        print(f"Position: {position}, f(n) = {f_value}")
else:
    print("No path found")
