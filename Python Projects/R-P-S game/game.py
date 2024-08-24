from tkinter import *
import random
from tkinter import messagebox





option=("rock","paper","scissors")


root=Tk()
root.geometry("360x500")
root.title("To-do List Application")
root.resizable(False,False)
root.configure(bg='#C69DD2')



# Logic part

userInput=""
User_text=StringVar()
Comp_text=StringVar()
Output=StringVar()
Results=StringVar()

user_count = IntVar(value=0)
comp_count = IntVar(value=0)

def press(num):
    global userInput
    userInput=str(num)
    User_text.set(userInput)
    computer=random.choice(option)
    Comp_text.set(computer)
    
    user_data=User_text.get()
    comp_data=Comp_text.get()
    
  
    
    if user_data==comp_data:
        Output.set("Its a tie!")
          
    elif user_data=="rock" and comp_data =="scissors":
        Output.set("Yay! you win!")
        user_count.set(user_count.get() + 1)
    elif user_data=="paper" and comp_data =="rock":
        Output.set("Yay! you win!")
        user_count.set(user_count.get() + 1)
    elif user_data=="scissors" and comp_data =="paper":
        Output.set("Yay! you win!")
        user_count.set(user_count.get() + 1)
    else:
        Output.set("You Lose!")
        comp_count.set(comp_count.get() + 1)
        
    if user_count.get() == 5:
        Results.set("Congratulations! You won this round!")
        prompt_continue()
        
    elif comp_count.get() == 5:
        Results.set("Game Over! You Lose!")
        prompt_continue()
        
        
def prompt_continue():
    answer = messagebox.askyesno("Continue?", "Do you want to continue?")
    if answer:
        reset_game()
        Results.set("")
    else:
        root.quit() 

def reset_game():
    User_text.set("")
    Comp_text.set("")
    user_count.set(0)
    comp_count.set(0)
    Output.set("")
        
  
#Design part 

#buttons

buttonframe=Frame(root,pady=20,bg='#C69DD2')
buttonframe.pack()

labeltop=Label(buttonframe,text="Pick One:",bg='#C69DD2')
labeltop.grid(row=0,column=1)

buttonR=Button(buttonframe,text="Rock",width=10,height=1,padx=10,pady=5,bg='#D1E9F6',command=lambda: press("rock"))
buttonP=Button(buttonframe,text="Paper",width=10,height=1,padx=5,pady=5,bg='#CCD5AE',command=lambda: press("paper"))
buttonS=Button(buttonframe,text="Scissors",width=10,height=1,padx=5,pady=5,bg='#FFE9D0',command=lambda: press("scissors"))

buttonR.grid(row=1,column=0)
buttonP.grid(row=1,column=1)
buttonS.grid(row=1,column=2)




#Display the current result
Disframe=Frame(root,bg='#C69DD2')
Disframe.pack()


dislabel1=Label(Disframe,text="You Choose: ",height=2,width=20,bg='#C69DD2')
dislabel2=Label(Disframe,textvariable=User_text,height=2,width=20,bg='#D6DAC8')
dislabel1.grid(row=0, column=0)
dislabel2.grid(row=1, column=0)

comlabel1=Label(Disframe,text="Computer Choose: ",height=2,width=20,bg='#C69DD2')
comlabel2=Label(Disframe,textvariable=Comp_text,height=2,width=20,bg='#FFEFEF')
comlabel1.grid(row=0, column=1)
comlabel2.grid(row=1, column=1)

outputlabel1=Label(root,text="Output:",height=2,width=20,bg='#C69DD2')
outputlabel2=Label(root,textvariable=Output,height=2,width=20,bg='#A390E4')
outputlabel1.pack()
outputlabel2.pack()

#Display the scores going on

Scoreframe=Frame(root,bg='#C69DD2',pady=20)
Scoreframe.pack()

ScoreUser1=Label(Scoreframe,text="User:",height=1,width=10,bg='#C69DD2')
ScoreUser2=Label(Scoreframe,textvariable=user_count,height=2,width=20,bd=5,pady=10,bg='#D6DAC8')
ScoreUser1.grid(row=0,column=0)
ScoreUser2.grid(row=1,column=0)

ScoreComp1=Label(Scoreframe,text="Computer",height=1,width=10,bg='#C69DD2')
ScoreComp2=Label(Scoreframe,textvariable=comp_count,height=2,width=20,bd=5,pady=10,bg='#FFEFEF')
ScoreComp1.grid(row=0,column=1)
ScoreComp2.grid(row=1,column=1)

# this is the result after one round 
Endlabel1=Label(root,text="Results",height=2,width=20,bg='#C69DD2')
Endlabel2=Label(root,textvariable=Results,height=2,width=30,bg='#A390E4',font=("Arial", 12, "bold"))
Endlabel1.pack()
Endlabel2.pack()



root.mainloop()