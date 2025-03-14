class GameOfLife:
    def __init__(self):
        self.current_display = set()

    def next(self):
        
        # In order to optimize the neighbour counting, we create a map based only on the alive cells and their surrounding squares.
        neighbour_counts = {}
        for alive_cell in self.current_display:
            for col in range(3):
                for row in range(3):
                    checking_cell = (alive_cell[0] -1 + row, alive_cell[1] -1 + col)
                    neighbour_counts[checking_cell] = neighbour_counts.get(checking_cell, 0) + 1

        
        next_generation = set()
        for next_gen_cell in neighbour_counts:
            if next_gen_cell in self.current_display:
                # If the cell was already alive, it has been counted as his own neighbour, so we fix that before going on
                neighbour_counts[next_gen_cell] -= 1
                if neighbour_counts[next_gen_cell] in range(2, 4):
                    next_generation.add(next_gen_cell)
            else:
                if neighbour_counts[next_gen_cell] == 3:
                    next_generation.add(next_gen_cell)

        self.current_display = next_generation.copy()

if __name__ == "__main__":
    my_game = GameOfLife()
    my_game.current_display.add((5,4))
    my_game.current_display.add((5,5))
    my_game.current_display.add((5,6))

    my_game.next()
    print(my_game.current_display)
    my_game.next()
    print(my_game.current_display)
    my_game.next()
    print(my_game.current_display)
