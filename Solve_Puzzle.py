from PIL import Image, ImageTk
import tkinter as tk
import random

class PuzzleSolver:
    def __init__(self, master, original_pieces, rows, cols):
        self.master = master
        self.master.title("Puzzle Solver")

        self.rows = rows
        self.cols = cols

        # Original pieces and shuffled pieces
        self.original_pieces = original_pieces
        self.shuffled_pieces = original_pieces[:]
        self.shuffled_pieces.append(None)  # Add None at the end to represent the empty space

        # Create buttons for each piece
        self.buttons = []
        for i in range(rows):
            for j in range(cols):
                index = i * cols + j
                button = tk.Button(master, command=lambda idx=index: self.move_piece(idx))
                button.grid(row=i, column=j)
                self.buttons.append(button)

        # Update the buttons with shuffled pieces
        self.update_buttons()

    def update_buttons(self):
        for button, piece in zip(self.buttons, self.shuffled_pieces):
            if piece:
                photo = ImageTk.PhotoImage(piece)
                button.config(image=photo, width=piece.width, height=piece.height)
                button.image = photo
            else:
                # Display an empty space for the None value
                button.config(text="", width=10, height=5)

    def move_piece(self, index):
        empty_index = self.shuffled_pieces.index(None)
        if self.is_valid_move(index, empty_index):
            self.shuffled_pieces[index], self.shuffled_pieces[empty_index] = (
                self.shuffled_pieces[empty_index],
                self.shuffled_pieces[index],
            )
            self.update_buttons()
            if self.shuffled_pieces[:-1] == self.original_pieces:
                tk.messagebox.showinfo("Congratulations!", "Puzzle solved!")

    def is_valid_move(self, index, empty_index):
        i, j = divmod(index, self.cols)
        empty_i, empty_j = divmod(empty_index, self.cols)
        return (abs(i - empty_i) == 1 and j == empty_j) or (i == empty_i and abs(j - empty_j) == 1)



def main():
    image_path = 'C://Users//Judeg//Downloads//Puzzle2.jpg'  # Replace with the path to your shuffled image
    rows = 3
    cols = 3

    original_image = Image.open(image_path)
    width, height = original_image.size
    piece_width = width // cols
    piece_height = height // rows

    original_pieces = [original_image.crop((j * piece_width, i * piece_height, (j + 1) * piece_width, (i + 1) * piece_height))
                       for i in range(rows) for j in range(cols)]

    root = tk.Tk()
    app = PuzzleSolver(root, original_pieces, rows, cols)

    root.mainloop()

if __name__ == "__main__":
    main()
