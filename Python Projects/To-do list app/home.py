from tkinter import *
from tkinter import ttk


class todo:
    def __init__(self, root):
                
        
        self.root =root
        self.root.geometry("380x500")
        self.root.title("To-do List Application")
        self.root.resizable(False,False)
        self.root.configure(bg='#DFD3C3')

        self.is_editing = False
        self.edit_index = None
        
        self.toplabel=Label(self.root,text="To-do List",font='ariel, 25',bg='#EF5A6F',fg='#F8EDE3')
        self.toplabel.pack(side='top',fill=BOTH)
        
        
        self.label1=Label(self.root,text="Add Task Here",font='ariel,30',bg='#DFD3C3',fg='#C5705D')
        self.label1.place(x=30,y=60)
        
        self.text=Text(self.root,bd=2,height=1,width=16,bg='#F8EDE3',font='ariel, 18')
        self.text.place(x=30,y=100)
        self.text.bind("<Return>", self.add)
        # self.text.bind("<Return>", self.add)
        
        
        self.label2=Label(self.root,text="Added Tasks",font='ariel,25 ',bg='#DFD3C3',fg='#C5705D')
        self.label2.place(x=30,y=170)
        
        self.main_text=Listbox(self.root,bg='#F8EDE3',height=7,bd=2,width=28,font='ariel,23')
        self.main_text.place(x=30,y=200)
        
        self.addbutton=Button(self.root,text="Add to list", font='sarif, 12 ',height=1,width=10,bd=2,bg='#D0B8A8',fg='#C5705D',cursor='hand2',command=self.add)
        self.addbutton.place(x=260,y=101)   
            
        self.delbutton1=Button(self.root,text="EDIT", font='sarif, 10 italic bold',height=2,width=10,bd=2,bg='blue',fg='white',cursor='hand2',command=self.start_editing)
        self.delbutton1.place(x=30,y=390)
        
        self.delbutton1=Button(self.root,text="DELETE", font='sarif, 10 italic bold',height=2,width=10,bd=2,bg='red',fg='white',cursor='hand2',command=self.delete)
        self.delbutton1.place(x=140,y=390)
        
        self.delbutton2=Button(self.root,text="DELETE ALL", font='sarif, 10 italic bold',height=2,width=10,bd=2,bg='red',fg='white',cursor='hand2',command=self.delete_all)
        self.delbutton2.place(x=255,y=390)
        
        self.massage=Label(self.root,text="** Please select One option to Edit or delete!")
        self.massage.place(x=70,y=450)
    
    
    #Functions    
    def add(self,event=None):
            content = self.text.get(1.0, END).strip()
            if content:
                if self.is_editing:
                    self.main_text.delete(self.edit_index)
                    self.main_text.insert(self.edit_index, f"• {content}")
                    self.update_file()
                    self.is_editing = False
                    self.edit_index = None
                    self.addbutton.config(text="Add to list")
                else:
                    self.main_text.insert(END, f"• {content}")
                    with open('data.txt', 'a') as file:
                        file.write(f"• {content}\n")
                self.text.delete(1.0, END)


    def start_editing(self):
            selected_index = self.main_text.curselection()
            if selected_index:
                self.edit_index = selected_index[0]
                task = self.main_text.get(self.edit_index)
                self.text.delete(1.0, END)
                self.text.insert(END, task[2:])  # Remove the bullet point before inserting
                self.is_editing = True
                self.addbutton.config(text="Update task")


    def delete(self):
            delete_ = self.main_text.curselection()
            if delete_:
                task = self.main_text.get(delete_)
                self.main_text.delete(delete_)
                self.update_file()

  
    def delete_all(self):
            self.main_text.delete(0, END)
            with open('data.txt', 'w') as file:
                file.truncate()

     
    def update_file(self):
            with open('data.txt', 'w') as file:
                tasks = self.main_text.get(0, END)
                for task in tasks:
                    file.write(f"{task}\n")

    
def main():
    root = Tk()
    ui=todo(root)
    root.mainloop()
    
if __name__=="__main__":
    main()