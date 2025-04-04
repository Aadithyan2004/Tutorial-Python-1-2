import tkinter as tk
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        
        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.guess_count += 1
            
            if guess < 1 or guess > 100:
                self.result_label.config(text="Please enter a number between 1 and 100.")
            elif guess < self.target_number:
                self.result_label.config(text="Too small, try again.")
            elif guess > self.target_number:
                self.result_label.config(text="Too large, try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed it in {self.guess_count} tries.")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Please enter a valid integer.")

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        self.entry.delete(0, tk.END)


root = tk.Tk()
game = GuessTheNumberGame(root)

root.mainloop()