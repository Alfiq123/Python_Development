# import tkinter as tk
# import random

# app = tk.Tk()
# app.title("Canvas")
# app.resizable(width = False, height = False)

# canvas = tk.Canvas(master = app, width = 500, height = 500, background = "#333333")
# canvas.pack(padx = 10, pady = 10)

# canvas.create_line((0, 0, 500, 500), fill = "#DCA06D", width = 5)
# canvas.create_line((0, 500, 500, 0), fill = "#DCA06D", width = 5)

# canvas.create_oval((0, 0, 500, 500), fill = "#4F1C51", outline = "#DCA06D", width = 5)

# canvas.create_rectangle((100, 100, 400, 400), fill = "#282828", outline = "#DCA06D", width = 5)

# canvas_points = [(250, 0), (500, 500), (0, 500)]
# canvas.create_polygon(canvas_points, fill = "#DCA06D", outline = "#DCA06D", width = 5)

# app_icon = tk.PhotoImage(file = "Python_Project/Icon_Python.png")
# app.iconphoto(True, app_icon)
# app.mainloop()

# import tkinter as tk
# import random

# def create_cool_canvas():
#     """Creates a visually appealing canvas with random shapes and colors."""

#     app = tk.Tk()
#     app.title("Cool Canvas")
#     app.resizable(width=False, height=False)

#     canvas_width = 600
#     canvas_height = 600
#     canvas = tk.Canvas(master=app, width=canvas_width, height=canvas_height, background="#222222")  # Dark background
#     canvas.pack(padx=20, pady=20)

#     # --- Helper Functions ---

#     def random_color():
#         """Generates a random hexadecimal color code."""
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#         return f"#{r:02x}{g:02x}{b:02x}"

#     def random_coordinates(max_x, max_y, min_size=20, max_size=150):
#         """Generates random coordinates and size for shapes."""
#         x1 = random.randint(0, max_x)
#         y1 = random.randint(0, max_y)
#         size = random.randint(min_size, max_size)
#         x2 = x1 + size
#         y2 = y1 + size
#         return x1, y1, x2, y2

#     # --- Draw Shapes ---

#     # 1. Concentric Circles
#     center_x = canvas_width // 2
#     center_y = canvas_height // 2
#     for i in range(5):
#         radius = 50 + i * 30
#         canvas.create_oval(
#             center_x - radius,
#             center_y - radius,
#             center_x + radius,
#             center_y + radius,
#             outline=random_color(),
#             width=3,
#         )

#     # 2. Random Rectangles
#     for _ in range(20):
#         x1, y1, x2, y2 = random_coordinates(canvas_width, canvas_height)
#         canvas.create_rectangle(
#             x1, y1, x2, y2, fill=random_color(), outline=""
#         )

#     # 3. Diagonal Lines
#     for _ in range(10):
#         x1 = random.randint(0, canvas_width)
#         y1 = random.randint(0, canvas_height)
#         x2 = random.randint(0, canvas_width)
#         y2 = random.randint(0, canvas_height)
#         canvas.create_line(x1, y1, x2, y2, fill=random_color(), width=2)

#     # 4. Scattered Ovals
#     for _ in range(15):
#         x1, y1, x2, y2 = random_coordinates(canvas_width, canvas_height, min_size=10, max_size=80)
#         canvas.create_oval(
#             x1, y1, x2, y2, fill=random_color(), outline=""
#         )
    
#     # 5. Polygon
#     for _ in range(3):
#         points = []
#         for _ in range(random.randint(3, 6)):
#             points.append(random.randint(0, canvas_width))
#             points.append(random.randint(0, canvas_height))
#         canvas.create_polygon(points, fill=random_color(), outline=random_color(), width=2)

#     # --- Add a Title ---
#     canvas.create_text(
#         canvas_width // 2,
#         30,
#         text="Abstract Art",
#         fill="#EEEEEE",  # Light text color
#         font=("Helvetica", 24, "bold"),
#     )

#     # --- Run the App ---
#     app_icon = tk.PhotoImage(file="Python_Project/Icon_Python.png")
#     app.iconphoto(True, app_icon)
#     app.mainloop()

# # Run the function to create the canvas
# create_cool_canvas()

import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        root.title("Simple Paint App")

        self.brush_color = "black"
        self.brush_size = 2

        self.canvas = tk.Canvas(root, bg="white", height=500, width=500)
        self.canvas.pack(pady=10)

        self.canvas.bind("<B1-Motion>", self.paint)

        # Color Palette Frame
        color_frame = tk.Frame(root)
        color_frame.pack(pady=5)

        colors = ["black", "red", "blue", "green", "yellow", "orange", "purple", "white"]
        for color in colors:
            color_button = tk.Button(color_frame, bg=color, width=2, height=1, command=lambda c=color: self.change_color(c))
            color_button.pack(side=tk.LEFT, padx=2)

        # Size Scale
        size_frame = tk.Frame(root)
        size_frame.pack(pady=5)
        size_label = tk.Label(size_frame, text="Brush Size:")
        size_label.pack(side=tk.LEFT)
        self.size_scale = tk.Scale(size_frame, from_=1, to=10, orient=tk.HORIZONTAL, command=self.change_size)
        self.size_scale.set(self.brush_size) # Set initial size
        self.size_scale.pack(side=tk.LEFT)

        # Clear Button
        clear_button = tk.Button(root, text="Clear Canvas", command=self.clear_canvas)
        clear_button.pack(pady=5)


    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

    def change_color(self, color):
        self.brush_color = color

    def change_size(self, size):
        self.brush_size = int(size) # Scale returns string, convert to int

    def clear_canvas(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
