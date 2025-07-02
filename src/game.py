class Cell:
    def __init__(self, state: bool):
        # True = alive, False = dead
        self.state = state

class Game:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[Cell(False) for _ in range(width)] for _ in range(height)]
        
    def count_alive_neighbors(self, x: int, y: int) -> int:
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.height and 0 <= ny < self.width:
                    if self.grid[nx][ny].state:
                        count += 1
        return count

    def update(self) -> None:
        new_grid = [[Cell(False) for _ in range(self.width)] for _ in range(self.height)]
        for x in range(self.height):
            for y in range(self.width):
                alive = self.grid[x][y].state
                neighbors = self.count_alive_neighbors(x, y)

                if alive and neighbors in (2, 3):
                    new_grid[x][y].state = True
                elif not alive and neighbors == 3:
                    new_grid[x][y].state = True
                else:
                    new_grid[x][y].state = False

        self.grid = new_grid
