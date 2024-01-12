import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.geometry("400x400")
        self.canvas = tk.Canvas(self.master, bg="black", width=400, height=400)
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.score = 0
        self.food_position = self.create_food()

        self.master.bind("<Key>", self.change_direction)
        self.move()

    def create_food(self):
        x = random.randrange(1, 39) * 10
        y = random.randrange(1, 39) * 10
        self.food = self.canvas.create_oval(x, y, x + 10, y + 10, fill="red")
        return x, y

    def move(self):
        head = self.snake[0]
        if self.direction == "Right":
            new_head = (head[0] + 10, head[1])
        elif self.direction == "Left":
            new_head = (head[0] - 10, head[1])
        elif self.direction == "Up":
            new_head = (head[0], head[1] - 10)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 10)

        self.snake.insert(0, new_head)

        if self.check_collision():
            self.game_over()
            return

        if new_head == (self.food_position[0], self.food_position[1]):
            self.score += 1
            self.canvas.delete(self.food)
            self.food_position = self.create_food()
        else:
            self.canvas.delete(self.snake[-1])
            self.snake.pop()

        self.draw_snake()
        self.master.after(100, self.move)

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", tags="snake")

    def change_direction(self, event):
        key = event.keysym
        if (key == "Right" and not self.direction == "Left") or \
           (key == "Left" and not self.direction == "Right") or \
           (key == "Up" and not self.direction == "Down") or \
           (key == "Down" and not self.direction == "Up"):
            self.direction = key

    def check_collision(self):
        head = self.snake[0]
        return (head[0] < 0 or head[0] >= 400 or
                head[1] < 0 or head[1] >= 400 or
                head in self.snake[1:])

    def game_over(self):
        self.canvas.create_text(200, 200, text=f"Game Over\nYour Score: {self.score}", fill="white", font=("Helvetica", 16))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
