import tkinter as tk
from tkinter import messagebox
import Task2 as mm

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)
        self.create_widgets()
        self.update_buttons()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="white")
        self.frame.pack(padx=10, pady=10)

        self.status_label = tk.Label(self.frame, text="Your turn (X)", font=('Helvetica', 14), bg="white")
        self.status_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.frame, text=" ", font=('Helvetica', 20), height=2, width=5,
                                   command=lambda x=i, y=j: self.btn_click(x, y))
                button.grid(row=i + 1, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

        self.reset_button = tk.Button(self.frame, text="Reset", font=('Helvetica', 14), command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=(10, 0))

    def btn_click(self, x, y):
        if mm.human_turn(x, y):
            self.buttons[x][y]["text"] = "X"
            if mm.game_over(mm.board):
                self.end_game()
            else:
                self.status_label.config(text="Computer's turn (O)")
                self.root.after(500, self.ai_move)  # slight delay to simulate thinking

    def ai_move(self):
        mm.ai_turn()
        self.update_buttons()
        if mm.game_over(mm.board):
            self.end_game()
        else:
            self.status_label.config(text="Your turn (X)")

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                if mm.board[i][j] == mm.HUMAN:
                    self.buttons[i][j]["text"] = "X"
                elif mm.board[i][j] == mm.COMP:
                    self.buttons[i][j]["text"] = "O"
                else:
                    self.buttons[i][j]["text"] = " "

    def end_game(self):
        if mm.wins(mm.board, mm.HUMAN):
            messagebox.showinfo("Game Over", "You win!")
        elif mm.wins(mm.board, mm.COMP):
            messagebox.showinfo("Game Over", "Computer wins!")
        else:
            messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        mm.reset_game()
        self.update_buttons()
        self.status_label.config(text="Your turn (X)")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
