import random
import tkinter as tk
from tkinter import messagebox
from tkinter import font

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!",0,0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!",1,0
    else:
        return "Computer wins!",0,1

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result, user_score_change, computer_score_change = determine_winner(user_choice, computer_choice)
    user_score += user_score_change
    computer_score += computer_score_change
    
    result=f"Your Choice:{user_choice}\nComputer chose: {computer_choice}\n\n{result}"
    result_label.config(text=result)
    score_label.config(text=f"User: {user_score}   Computer: {computer_score}")  # Update the score label
def show_game_log():
    game_log = "Rock, Paper, Scissors Game Log:\n\n" \
               "Rock crushes Scissors.\n" \
               "Scissors cuts Paper.\n" \
               "Paper covers Rock."
    messagebox.showinfo("Game Logic", game_log)

def main():
    root = tk.Tk()
    root.minsize(400,600)
    root.maxsize(400,600)

    root.configure(bg="gray")
    root.title("Rock Paper Scissors Game")

    title_label = tk.Label(root, text="Rock--Paper--Scissors", font=("Arial", 12,"bold"),bg="lightgray",height=3)
    title_label.config(width=400)
    title_label.pack()
    title_label1 = tk.Label(root, text="GAME", font=("Poppins", 18,"bold"),bg="lightgray")
    title_label1.config(width=400)
    title_label1.pack()
    global user_score,computer_score
    user_score=0
    computer_score=0
    def button_click(choice):
        play_game(choice)
    custom_font=("Poppins",12)
    rock_button = tk.Button(root, text="Rock", command=lambda: button_click("rock"),font=custom_font, bg="blue", fg="white", width=18, height=2, bd=2)
    rock_button.pack(pady=10)

    paper_button = tk.Button(root, text="Paper", command=lambda: button_click("paper"),font=custom_font,bg="green", fg="white", width=18, height=2, bd=2)
    paper_button.pack(pady=10)

    scissors_button = tk.Button(root, text="Scissors", command=lambda: button_click("scissors"),font=custom_font,bg="red", fg="white", width=18, height=2, bd=2)
    scissors_button.pack(pady=10)


    result_title_label1 = tk.Label(root, text="RESULT", font=("Poppins", 18,"bold"),bg="lightgray",border=2)
    result_title_label1.config(width=400)
    result_title_label1.pack()

    global result_label,score_label
    result_label = tk.Label(root, font=("Arial", 14),height=4, pady=10)
    result_label.config(width=400)
    result_label.pack()

    # Create a menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # Create a "Help" menu
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="Game Logic", command=show_game_log)
    menubar.add_cascade(label="Help", menu=help_menu)
    
    # Create label for displaying score
    score_label = tk.Label(root, font=("Arial", 14), pady=10,bg="gray")
    score_label.pack()
    score_label.config(text=f"Your Score: {user_score}   Computer Score: {computer_score}")
    root.mainloop()

if __name__ == "__main__":
    main()
