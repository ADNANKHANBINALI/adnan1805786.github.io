from tkinter import *
from tkinter.messagebox import *
#some font variable
font=('verdana',15,'bold')           #'bold underline' to underline all label
#button binding
def all_clear():
    textField.delete(0,END)

def clear():
    ex=textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)
    textField.delete(0)
    
def click_btn_function(event):
    print('btn clicked')
    b=event.widget
    text =b['text']
    print(text)

    if text =='x':
        textField.insert(END,'*')
        return
    
    if text == '=':
        try:
             ex = textField.get()
             anser=eval(ex)
             textField.delete(0,END)
             textField.insert(0,anser)
        except Exception as e:
                 print('Error..',e)
                 showerror('Error...',e)
                 textField.delete(0,END)
                 textField.insert(0)
        return
    
    
    textField.insert(END,text)
#creating a window
window=Tk()
window.title('CALCULATOR')
window.geometry('10x10')
#picture label
'''pic = PhotoImage(file='')
headinglabel =Label(window,image=pic)
headinglabel.pack(side=TOP,pady=15)'''
#heading label
heading=Label(window,text="Adnan's calculator",font=font,underline=7)
heading.pack(side=TOP)
#text filed
textField=Entry(window,font=font,justify=CENTER)
textField.pack(side=TOP,pady=5, fill=X,padx=10)
#buttons
buttonFrame= Frame(window)
buttonFrame.pack(side=TOP)
# adding button
'''btn1 = Button(buttonFrame,text='1',font=font)
btn1.pack(side=TOP)
btn2 = Button(buttonFrame,text='2',font=font)
btn2.pack(side=TOP)'''
temp=9
for i in range(1,4):
    for j in range(0,3):
       btn = Button(buttonFrame,text=str(temp),font=font,width=3,activebackground='orange',activeforeground='white',background='white')
       btn.grid(row=i,column=j)
       temp = temp - 1
       btn.bind('<Button-1>', click_btn_function)
zerobtn = Button(buttonFrame,text='0',font=font,width=3,activebackground='orange',activeforeground='white',background='white')
zerobtn.grid(row=4,column=1)
dtbtn = Button(buttonFrame,text='.',font=font,width=3,activebackground='orange',activeforeground='white',background='white')
dtbtn.grid(row=4,column=2)     
eqbtn = Button(buttonFrame,text='=',font=font,width=3,activebackground='white',activeforeground='orange',foreground='white',background='orange')
eqbtn.grid(row=4,column=3)
clearbtn = Button(buttonFrame,text='C',font=font,width=3,activebackground='orange',activeforeground='white',background='white',foreground='orange',command=clear)
clearbtn.grid(row=0,column=1)
allclearbtn = Button(buttonFrame,text='A.C',font=font,width=3,activebackground='orange',activeforeground='white',background='white',foreground='orange',command=all_clear)
allclearbtn.grid(row=0,column=0)
exbtn = Button(buttonFrame,text='ex',font=font,width=3,activebackground='orange',activeforeground='white',foreground='orange',background='white')
exbtn.grid(row=4,column=0)

plbtn = Button(buttonFrame,text='+',font=font,width=3,foreground='orange',activebackground='orange',activeforeground='white',background='white')
plbtn.grid(row=3,column=3)
mnbtn = Button(buttonFrame,text='-',font=font,width=3,foreground='orange',activebackground='orange',activeforeground='white',background='white')
mnbtn.grid(row=2,column=3)
mubtn = Button(buttonFrame,text='x',font=font,width=3,foreground='orange',activebackground='orange',activeforeground='white',background='white')
mubtn.grid(row=1,column=3)
dybtn = Button(buttonFrame,text='/',font=font,width=3,foreground='orange',activebackground='orange',activeforeground='white',background='white')
dybtn.grid(row=0,column=3)


#left button binding

exbtn.bind('<Button-1>', click_btn_function)
clearbtn.bind('<Button-1>', click_btn_function)
eqbtn.bind('<Button-1>', click_btn_function)
dtbtn.bind('<Button-1>', click_btn_function)
zerobtn.bind('<Button-1>', click_btn_function)
plbtn.bind('<Button-1>', click_btn_function)
mnbtn.bind('<Button-1>', click_btn_function)
mubtn.bind('<Button-1>', click_btn_function)
dybtn.bind('<Button-1>', click_btn_function)
allclearbtn.bind('<Button-1>', click_btn_function)

window.mainloop()