from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title('Uncle Flashcard by Uncle Engineer')
GUI.geometry('600x600')
# GUI.state('zoomed')
GUI.resizable(0,0)

FONT1 = ('Angsana New',40,'bold')
FONT2 = ('Angsana New',100)

vocab = ['Cat','Dog','Bird','Python คือ?']
answer = ['แมว','หมา','นก','คือภาษาเขียนโปรแกรมชนิดหนึ่ง']
count_vocab = len(vocab)
global count
count = 0

L = Label(GUI,text='Cat',font=FONT1,fg='green')
L.pack(pady=50)

L2 = Label(GUI,text='แมว',font=FONT1,fg='blue')


# --------------------------
def Next():
    global count
    if count < count_vocab and count != count_vocab-1:
        count = count + 1
    print(count)
    L.configure(text=vocab[count])
    L2.configure(text=answer[count])
    

F1 = Frame(GUI)
F1.place(x=500,y=500)
B = ttk.Button(F1,text='>',command=Next)
B.pack(ipady=20)
# --------------------------
def Prev():
    global count
    if count > 0:
        count = count - 1
    print(count)
    L.configure(text=vocab[count])
    L2.configure(text=answer[count])
    
    
F2 = Frame(GUI)
F2.place(x=30,y=500)
B = ttk.Button(F2,text='<',command=Prev)
B.pack(ipady=20)
# --------------------------
state_answer = True
def Answer():
    global state_answer
    if state_answer == True:
        # showing
        BA.configure(text='Hide')
        state_answer = False
        L2.pack(pady=50)
        L2.configure(text=answer[count])
        
    else:
        BA.configure(text='Answer')
        state_answer = True
        L2.pack_forget()
        
F3 = Frame(GUI)
F3.place(x=250,y=500)
BA = ttk.Button(F3,text='Answer',command=Answer)
BA.pack(ipady=20,ipadx=20)

GUI.mainloop()
