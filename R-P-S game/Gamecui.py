# import random

# option=("rock","paper","scissors")
# running =True

# while running:
    
#     player=None
#     computer=random.choice(option)
    
#     while player not in option:
#         player=input("Enter a choice:")
    

#     print(f"Player:{player}")
#     print(f"Computer:{computer}")


#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer=="scissors":
#         print("Yay! you wins!")
#     elif player == "paper" and computer=="rock":
#         print("Yay! you wins!")
#     elif player == "scissors" and computer=="paper":
#         print("Yay! you wins!")
#     else:
#         print("Computer wins! You lose!")
        
#     play_again=print("Do you want to play again(y/n)" )
#     if not play_again=="y":
#         running=False
    
# print("Thanks for playing")

from tkinter import *
from tkinter import messagebox
import random

option = ("rock", "paper", "scissors")

root = Tk()
root.geometry("360x480")
root.title("Rock, Paper, Scissors Game")
root.resizable(False, False)
root.configure(bg="#2E2E2E")

userInput = ""
User_text = StringVar()
Comp_text = StringVar()
Output = StringVar()
Results = StringVar()

# Initialize the score variables
user_count = IntVar(value=0)
comp_count = IntVar(value=0)

def press(num):
    global userInput
    userInput = str(num)
    User_text.set(userInput)
    computer = random.choice(option)
    Comp_text.set(computer)
    
    user_data = User_text.get()
    comp_data = Comp_text.get()
    
    if user_data == comp_data:
        Output.set("It's a tie!")
    elif (user_data == "rock" and comp_data == "scissors") or \
         (user_data == "paper" and comp_data == "rock") or \
         (user_data == "scissors" and comp_data == "paper"):
        Output.set("Yay! You win!")
        user_count.set(user_count.get() + 1)  # Update user score
    else:
        Output.set("You lose!")
        comp_count.set(comp_count.get() + 1)  # Update computer score
    
    # Check if either player has reached 5 points
    if user_count.get() == 5:
        Results.set("Congratulations! You won this round!")
        root.after(1000, prompt_continue)  # Ask if user wants to continue after 1 second
    elif comp_count.get() == 5:
        Results.set("Game Over! The computer won this round!")
        root.after(1000, prompt_continue)  # Ask if user wants to continue after 1 second

def prompt_continue():
    # Ask the user if they want to continue playing
    answer = messagebox.askyesno("Continue?", "Do you want to continue?")
    if answer:
        reset_game()  # Reset game if user says "Yes"
    else:
        root.quit()  # Close the application if user says "No"

def reset_game():
    # Reset the scores for a new round
    user_count.set(0)
    comp_count.set(0)
    Output.set("")
    Results.set("")  # Clear the Results tab

buttonframe = Frame(root, pady=20, bg="#2E2E2E")
buttonframe.pack()

labeltop = Label(buttonframe, text="Pick One:", font=("Arial", 12), fg="#FFD700", bg="#2E2E2E")
labeltop.grid(row=0, column=1)

buttonR = Button(buttonframe, text="Rock", width=10, height=1, padx=10, pady=5, 
                 bg="#FF6347", fg="#FFFFFF", font=("Arial", 10, "bold"), command=lambda: press("rock"))
buttonP = Button(buttonframe, text="Paper", width=10, height=1, padx=5, pady=5, 
                 bg="#4682B4", fg="#FFFFFF", font=("Arial", 10, "bold"), command=lambda: press("paper"))
buttonS = Button(buttonframe, text="Scissors", width=10, height=1, padx=5, pady=5, 
                 bg="#32CD32", fg="#FFFFFF", font=("Arial", 10, "bold"), command=lambda: press("scissors"))

buttonR.grid(row=1, column=0)
buttonP.grid(row=1, column=1)
buttonS.grid(row=1, column=2)

# Display
Disframe = Frame(root, bg="#2E2E2E")
Disframe.pack()

dislabel1 = Label(Disframe, text="You Choose:", height=2, width=20, fg="#FFD700", bg="#2E2E2E", font=("Arial", 10))
dislabel2 = Label(Disframe, textvariable=User_text, bg="#000000", fg="#FFD700", height=2, width=20, bd=5, font=("Arial", 10))
dislabel1.grid(row=0, column=0)
dislabel2.grid(row=1, column=0)

comlabel1 = Label(Disframe, text="Computer Choose:", height=2, width=20, fg="#FFD700", bg="#2E2E2E", font=("Arial", 10))
comlabel2 = Label(Disframe, textvariable=Comp_text, bg="#000000", fg="#FFD700", height=2, width=20, bd=5, font=("Arial", 10))
comlabel1.grid(row=0, column=1)
comlabel2.grid(row=1, column=1)

outputlabel1 = Label(root, text="Output:", height=2, width=20, fg="#FFD700", bg="#2E2E2E", font=("Arial", 10))
outputlabel2 = Label(root, textvariable=Output, bg="#000000", fg="#FFD700", height=2, width=20, bd=5, font=("Arial", 10))
outputlabel1.pack()
outputlabel2.pack()

# Score frame
Scoreframe = Frame(root, bg="#2E2E2E")
Scoreframe.pack()

ScoreUser1 = Label(Scoreframe, text="User:", height=1, width=10, fg="#FFD700", bg="#2E2E2E", font=("Arial", 10))
ScoreUser2 = Label(Scoreframe, textvariable=user_count, bg="#000000", fg="#FFD700", height=2, width=20, bd=5, pady=10, font=("Arial", 10))
ScoreUser1.grid(row=0, column=0)
ScoreUser2.grid(row=0, column=1)

ScoreComp1 = Label(Scoreframe, text="Computer:", height=1, width=10, fg="#FFD700", bg="#2E2E2E", font=("Arial", 10))
ScoreComp2 = Label(Scoreframe, textvariable=comp_count, bg="#000000", fg="#FFD700", height=2, width=20, bd=5, pady=10, font=("Arial", 10))
ScoreComp1.grid(row=1, column=0)
ScoreComp2.grid(row=1, column=1)

Endlabel1 = Label(root, text="Results", height=2, width=20, fg="#FFD700", bg="#2E2E2E", font=("Arial", 12, "bold"))
Endlabel2 = Label(root, textvariable=Results, bg="#000000", fg="#FFD700", height=2, width=20, bd=5, font=("Arial", 12, "bold"))
Endlabel1.pack()
Endlabel2.pack()

root.mainloop()
