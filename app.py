import tkinter as tk
from core import GameOfLife

# Base dimensions
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20

class GameOfLifeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game of Life - Conway")

        self.canvas = tk.Canvas(root, width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE, bg='white')
        self.canvas.pack()

        self.running = False

        # The core gets initialized
        self.game = GameOfLife()

        # Connecting the cells as buttons for adding or deleteing them of the core
        self.canvas.bind("<Button-1>", self.toggle_cell)

        # Control buttons
        self.start_button = tk.Button(root, text="Play", command=self.start)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(root, text="Pause", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(root, text="Clean", command=self.clear)
        self.clear_button.pack(side=tk.LEFT)
        
        # First display
        self.update_canvas()

    def toggle_cell(self, event):
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE
        pos = (x, y)
        
        # If the cell is already there it just gets removed
        if pos in self.game.current_display:
            self.game.current_display.remove(pos)
        else:
            self.game.current_display.add(pos)

        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")

        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                # Canvas restrictions
                if x < GRID_WIDTH and y < GRID_HEIGHT:
                    color = 'black' if (x, y) in self.game.current_display else 'white'

                    self.canvas.create_rectangle(
                        x * CELL_SIZE, y * CELL_SIZE,
                        (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                        fill=color, outline='gray'
                    )

    def start(self):
        if not self.running:
            self.running = True
            self.run_simulation()

    def stop(self):
        self.running = False

    def clear(self):
        self.running = False
        self.game = GameOfLife()  # Reset the core
        self.update_canvas()

    def run_simulation(self):
        if self.running:
            self.game.next()
            self.update_canvas()
            self.root.after(200, self.run_simulation)  # 200 ms per iteration


root = tk.Tk()
app = GameOfLifeApp(root)
root.mainloop()
