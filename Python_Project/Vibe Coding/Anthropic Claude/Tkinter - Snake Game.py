import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)
        
        # Game constants
        self.WIDTH = 600
        self.HEIGHT = 400
        self.GRID_SIZE = 20
        self.GAME_SPEED = 100  # Milliseconds
        
        # Game state
        self.direction = "Right"
        self.next_direction = "Right"
        self.running = False
        self.score = 0
        
        # Initialize snake and food
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()
        
        # Create canvas
        self.canvas = tk.Canvas(root, width=self.WIDTH, height=self.HEIGHT, bg="black")
        self.canvas.pack(padx=10, pady=10)
        
        # Score label
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 12))
        self.score_label.pack(pady=5)
        
        # Control buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)
        
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_game)
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause_game, state=tk.DISABLED)
        self.pause_button.grid(row=0, column=1, padx=5)
        
        self.restart_button = tk.Button(button_frame, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=0, column=2, padx=5)
        
        # Bind keys
        self.root.bind("<Left>", lambda event: self.change_direction("Left"))
        self.root.bind("<Right>", lambda event: self.change_direction("Right"))
        self.root.bind("<Up>", lambda event: self.change_direction("Up"))
        self.root.bind("<Down>", lambda event: self.change_direction("Down"))
        
        # Draw initial screen
        self.draw_welcome_screen()
    
    def draw_welcome_screen(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            self.WIDTH // 2, 
            self.HEIGHT // 2 - 30, 
            text="Welcome to Snake Game!", 
            fill="white", 
            font=("Arial", 20)
        )
        self.canvas.create_text(
            self.WIDTH // 2, 
            self.HEIGHT // 2 + 10, 
            text="Use arrow keys to move", 
            fill="white", 
            font=("Arial", 14)
        )
        self.canvas.create_text(
            self.WIDTH // 2, 
            self.HEIGHT // 2 + 40, 
            text="Press Start to begin", 
            fill="white", 
            font=("Arial", 14)
        )
    
    def draw_game_over_screen(self):
        self.canvas.create_rectangle(
            self.WIDTH // 2 - 100, 
            self.HEIGHT // 2 - 60, 
            self.WIDTH // 2 + 100, 
            self.HEIGHT // 2 + 60, 
            fill="black", 
            outline="red"
        )
        self.canvas.create_text(
            self.WIDTH // 2, 
            self.HEIGHT // 2 - 30, 
            text="Game Over!", 
            fill="red", 
            font=("Arial", 20)
        )
        self.canvas.create_text(
            self.WIDTH // 2, 
            self.HEIGHT // 2 + 10, 
            text=f"Final Score: {self.score}", 
            fill="white", 
            font=("Arial", 14)
        )
    
    def create_food(self):
        while True:
            x = random.randint(1, (self.WIDTH - self.GRID_SIZE) // self.GRID_SIZE) * self.GRID_SIZE
            y = random.randint(1, (self.HEIGHT - self.GRID_SIZE) // self.GRID_SIZE) * self.GRID_SIZE
            
            # Make sure food doesn't appear on the snake
            if (x, y) not in self.snake:
                return (x, y)
    
    def change_direction(self, new_direction):
        # Prevent 180-degree turns
        opposite_directions = {
            "Left": "Right",
            "Right": "Left",
            "Up": "Down",
            "Down": "Up"
        }
        
        if new_direction != opposite_directions.get(self.direction):
            self.next_direction = new_direction
    
    def move_snake(self):
        if not self.running:
            return
        
        # Update direction
        self.direction = self.next_direction
        
        # Get current head position
        head_x, head_y = self.snake[0]
        
        # Calculate new head position
        if self.direction == "Left":
            new_head = (head_x - self.GRID_SIZE, head_y)
        elif self.direction == "Right":
            new_head = (head_x + self.GRID_SIZE, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - self.GRID_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + self.GRID_SIZE)
        
        # Check for collision with walls
        new_x, new_y = new_head
        if (new_x < 0 or new_x >= self.WIDTH or 
            new_y < 0 or new_y >= self.HEIGHT):
            self.game_over()
            return
        
        # Check for collision with self
        if new_head in self.snake:
            self.game_over()
            return
        
        # Add new head to snake
        self.snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")
            self.food = self.create_food()
            
            # Speed up the game slightly as score increases
            new_speed = max(50, self.GAME_SPEED - (self.score // 50))
            self.GAME_SPEED = new_speed
        else:
            # Remove tail if no food eaten
            self.snake.pop()
        
        # Draw everything
        self.draw_game_state()
        
        # Schedule next move
        self.root.after(self.GAME_SPEED, self.move_snake)
    
    def draw_game_state(self):
        self.canvas.delete("all")
        
        # Draw snake
        for i, (x, y) in enumerate(self.snake):
            color = "#00FF00" if i == 0 else "#00CC00"  # Head is slightly different color
            self.canvas.create_rectangle(
                x, y, 
                x + self.GRID_SIZE, y + self.GRID_SIZE, 
                fill=color, outline=""
            )
        
        # Draw food
        food_x, food_y = self.food
        self.canvas.create_oval(
            food_x, food_y, 
            food_x + self.GRID_SIZE, food_y + self.GRID_SIZE, 
            fill="red", outline=""
        )
    
    def start_game(self):
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.move_snake()
    
    def pause_game(self):
        if self.running:
            self.running = False
            self.pause_button.config(text="Resume")
        else:
            self.running = True
            self.pause_button.config(text="Pause")
            self.move_snake()
    
    def restart_game(self):
        self.running = False
        self.direction = "Right"
        self.next_direction = "Right"
        self.score = 0
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()
        self.GAME_SPEED = 100
        
        self.score_label.config(text=f"Score: {self.score}")
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(text="Pause", state=tk.DISABLED)
        
        self.draw_welcome_screen()
    
    def game_over(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(text="Pause", state=tk.DISABLED)
        self.draw_game_over_screen()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
