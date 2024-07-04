from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x650")
root.resizable(False,False)

root.configure(bg="grey")
your_score=0
computer_score=0
def clear():
    global result
    result = ""
    label.config(text=result)

def start(user_choice):
    global your_score 
    global computer_score
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = ""


    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
          result = "You win!", 
          your_score = your_score+1
          
    else:
        result = "You lose!",
        computer_score=computer_score+1 
    
    label.config(text=f"Your choice: {user_choice}\n Computer choice: {computer_choice}\n your_score:{your_score}\ncomputer_score:{computer_score}\n{result}",bd=9,bg="powder blue")



label = Label(root, text="PLAY GAME", font=("arial 18 bold"),relief=SUNKEN,bd=9)
label.pack(pady=10,padx=5)

label = Label(root, text="CHOOSE ANY ONE", font=("arial 18 bold"),relief=SUNKEN,bd=9)
label.pack(pady=10,padx=5)

rock = Button(root, text="Rock",font=("arial 15 bold"),bd=9,fg="#fff",bg="#2a2d36", command=lambda: start("Rock")).pack(pady=10)
paper = Button(root, text="Paper",font=("arial 15 bold"),bd=9,fg="#fff",bg="#2a2d36", command=lambda: start("Paper")).pack(pady=10)
scissors = Button(root, text="Scissors",font=("arial 15 bold"),bd=9,fg="#fff",bg="#2a2d36", command=lambda: start("Scissors")).pack(pady=10)
new_game = Button(root, text="NEW_GAME",font=("arial 15 bold"),bd=9,fg="#fff",bg="#3697f5", command=lambda: clear()).pack(pady=10)
label = Label(root, text="", font=("arial 18 bold"),relief=SUNKEN,bd=9)
label.pack(pady=10)

root.mainloop()
