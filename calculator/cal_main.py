from tkinter import *

root=Tk()
root.geometry("360x480")
root.title("To-do List Application")
root.resizable(False,False)
root.configure(bg='#000000')

#variables to store the results

equation_value=""
equation_Str=StringVar()

#Funtions

def button_press(num):
    global equation_value
    equation_value += str(num)
    equation_Str.set(equation_value)
    
def equal():
    try:
        global equation_value
        total=str(eval(equation_value))
        equation_Str.set(total)
    except ZeroDivisionError:
        equation_Str.set("Arithmatic Error 🥱")
        equation_value=""
    except SyntaxError:
        equation_Str.set("Invalid Input 😑")
        equation_value=""
        
def clearAll():
    global equation_value
    equation_value = ""
    equation_Str.set(equation_value)
  

def key_press(event):
    key = event.char
    if key in '0123456789':
        button_press(key)
    elif key in '+-*/%':
        button_press(key)
    elif key == '\r':       # Enter key
        equal()
    elif key == '\b':       # Backspace key
        clearAll()
    elif key == '.':
        button_press('.')  
  

#frame1- to put the display label in place

frame_dis=Frame(root,padx=5,pady=10,bg='#000000')
frame_dis.pack(side="top")

label=Label(frame_dis,textvariable=equation_Str,font=('consolas',20),padx=5,pady=10,bg='#000000',fg='#ffffff',width=22,height=2)
label.pack(side='top')

#frame 2- to put the keyboard layout
frame_key=Frame(root,bg='#000000')
frame_key.pack(side="bottom")

#create button

button1=Button(frame_key,text=1,height=2,width=7,padx=2,pady=5,font=35,bg='#333333',fg='#ffffff',command=lambda: button_press(1))
button2=Button(frame_key,text=2,height=2,width=7,padx=2,pady=5,font=35,bg='#333333',fg='#ffffff',command=lambda: button_press(2))
button3=Button(frame_key,text=3,height=2,width=7,padx=2,pady=5,font=35,bg='#333333',fg='#ffffff',command=lambda: button_press(3))
button4=Button(frame_key,text=4,height=2,width=7,padx=2,pady=5,font=35,bg='#333333',fg='#ffffff',command=lambda: button_press(4))
button5=Button(frame_key,text=5,height=2,width=7,padx=2,pady=5,font=35,bg='#333333',fg='#ffffff',command=lambda: button_press(5))
button6=Button(frame_key,text=6,height=2,width=7,padx=2,pady=5,font=35,bg='#333333',fg='#ffffff',command=lambda: button_press(6))
button7=Button(frame_key,text=7,height=2,width=7,padx=2,pady=5,font=35,bg='#333333',fg='#ffffff',command=lambda: button_press(7))
button8=Button(frame_key,text=8,height=2,width=7,padx=2,pady=5,font=35,bg='#333333',fg='#ffffff',command=lambda: button_press(8))
button9=Button(frame_key,text=9,height=2,width=7,padx=2,pady=5,font=35,bg='#333333',fg='#ffffff',command=lambda: button_press(9))
button0=Button(frame_key,text=0,height=2,width=7,padx=2,pady=5,font=35,bg='#333333',fg='#ffffff',command=lambda: button_press(0))
button_openb=Button(frame_key,text="(",height=2,width=7,padx=2,pady=5,font=35,bg='#333333',fg='#ffffff',command=lambda: button_press('('))
button_closeb=Button(frame_key,text=')',height=2,width=7,padx=2,pady=5,font=35,bg='#333333',fg='#ffffff',command=lambda: button_press(")"))

button_add=Button(frame_key,text='+',height=2,width=7,bg='#222222',fg='#ffffff',font=35,padx=2,pady=5,command=lambda: button_press('+'))
button_sub=Button(frame_key,text='-',height=2,width=7,bg='#222222',fg='#ffffff',font=35,padx=2,pady=5,command=lambda: button_press('-'))
button_mul=Button(frame_key,text='*',height=2,width=7,bg='#222222',fg='#ffffff',font=35,padx=2,pady=5,command=lambda: button_press('*'))
button_div=Button(frame_key,text='/',height=2,width=7,bg='#222222',fg='#ffffff',font=35,padx=2,pady=5,command=lambda: button_press('/'))
button_eq=Button(frame_key,text='=',height=2,width=7,font=35,padx=2,pady=5,bg='#fb8500',fg='#ffffff',command=lambda: equal())

button_AC=Button(frame_key,text='AC',height=2,width=7,font=35,padx=2,pady=5,bg='#222222',fg='#ffffff',command=lambda: clearAll())
button_module=Button(frame_key,text='%',height=2,width=7,font=35,padx=2,pady=5,bg='#222222',fg='#ffffff',command=lambda: button_press('%'))
button_dot=Button(frame_key,text='.',height=2,width=7,font=35,padx=2,pady=5,bg='#222222',fg='#ffffff',command=lambda: button_press('.'))


#Buttons Positions

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button0.grid(row=4,column=1)
button_openb.grid(row=4,column=0)
button_closeb.grid(row=4,column=2)

button_add.grid(row=3,column=3)
button_sub.grid(row=2,column=3)
button_mul.grid(row=1,column=3)
button_eq.grid(row=4,column=3)

button_div.grid(row=0,column=3)
button_dot.grid(row=0,column=2)
button_module.grid(row=0,column=1)
button_AC.grid(row=0,column=0)


root.bind('<Key>', key_press)

root.mainloop()
