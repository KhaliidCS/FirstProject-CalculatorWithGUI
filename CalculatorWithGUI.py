##Calculator with GUI


import tkinter as tk
import _tkinter


calculation=""

def addToCalculaton(sympol):
    global calculation
    calculation+=str(sympol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calculation)


def EvaluateCalculaton():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")



def  clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0, "end")




def ClearCalculaton():
    pass


root=tk.Tk()
root.geometry("400x275")
text_result=tk.Text(root,height=2,width=16,font=("Arial",24))
text_result.grid(columnspan=5)

btn1=tk.Button(root,text="1",command=lambda :addToCalculaton(1),width=5,font=("Arial",14))
btn1.grid(row=2,column=1)

btn2=tk.Button(root,text="2",command=lambda :addToCalculaton(2),width=5,font=("Arial",14))
btn2.grid(row=2,column=2)

btn3=tk.Button(root,text="3",command=lambda :addToCalculaton(3),width=5,font=("Arial",14))
btn3.grid(row=2,column=3)

btn4=tk.Button(root,text="4",command=lambda :addToCalculaton(4),width=5,font=("Arial",14))
btn4.grid(row=3,column=1)

btn5=tk.Button(root,text="5",command=lambda :addToCalculaton(5),width=5,font=("Arial",14))
btn5.grid(row=3,column=2)

btn6=tk.Button(root,text="6",command=lambda :addToCalculaton(6),width=5,font=("Arial",14))
btn6.grid(row=3,column=3)

btn7=tk.Button(root,text="7",command=lambda :addToCalculaton(7),width=5,font=("Arial",14))
btn7.grid(row=4,column=1)

btn8=tk.Button(root,text="8",command=lambda :addToCalculaton(8),width=5,font=("Arial",14))
btn8.grid(row=4,column=2)

btn9=tk.Button(root,text="9",command=lambda :addToCalculaton(9),width=5,font=("Arial",14))
btn9.grid(row=4,column=3)

btn0=tk.Button(root,text="0",command=lambda :addToCalculaton(0),width=5,font=("Arial",14))
btn0.grid(row=5,column=2)

btnplus=tk.Button(root,text="+",command=lambda :addToCalculaton("+"),width=5,font=("Arial",14))
btnplus.grid(row=2,column=4)

btnsubtract=tk.Button(root,text="-",command=lambda :addToCalculaton("-"),width=5,font=("Arial",14))
btnsubtract.grid(row=3,column=4)

btnmultiply=tk.Button(root,text="*",command=lambda :addToCalculaton("*"),width=5,font=("Arial",14))
btnmultiply.grid(row=4,column=4)

btndivison=tk.Button(root,text="/",command=lambda :addToCalculaton("/"),width=5,font=("Arial",14))
btndivison.grid(row=5,column=4)

btnopen=tk.Button(root,text="(",command=lambda :addToCalculaton("("),width=5,font=("Arial",14))
btnopen.grid(row=5,column=1)

btnclose=tk.Button(root,text=")",command=lambda :addToCalculaton(")"),width=5,font=("Arial",14))
btnclose.grid(row=5,column=3)

btnequal=tk.Button(root,text="=",command=EvaluateCalculaton,width=12,font=("Arial",14))
btnequal.grid(row=6,column=1,columnspan=2)

btnclear=tk.Button(root,text="C",command=clear_field,width=12,font=("Arial",14))
btnclear.grid(row=6,column=3,columnspan=2)







