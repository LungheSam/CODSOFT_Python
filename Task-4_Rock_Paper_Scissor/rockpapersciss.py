import random
import tkinter as tk
from tkinter import messagebox
from tkinter import font

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    # messagebox.showinfo("Result", f"Your Choice:{user_choice}\nComputer chose: {computer_choice}\n{result}")
    result=f"Your Choice:{user_choice}\nComputer chose: {computer_choice}\n\n{result}"
    result_label.config(text=result)

def main():
    root = tk.Tk()
    root.minsize(400,580)
    root.maxsize(400,580)

    root.configure(bg="gray")
    root.title("Rock Paper Scissors Game")

    title_label = tk.Label(root, text="Rock--Paper--Scissors", font=("Arial", 12,"bold"),bg="lightgray",height=3)
    title_label.config(width=400)
    title_label.pack()
    title_label1 = tk.Label(root, text="GAME", font=("Poppins", 18,"bold"),bg="lightgray")
    title_label1.config(width=400)
    title_label1.pack()
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

    global result_label
    result_label = tk.Label(root, font=("Arial", 14),height=4, pady=10)
    result_label.config(width=400)
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
