from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("300x300")

name1=StringVar()
email1=StringVar()
a1=DoubleVar()
c1=IntVar()
c2=IntVar()
c3=IntVar()
r1=IntVar()

def getDetails():
    str1="Name: "+str(name1.get())+"\n"
    str1+="Email: "+str(email1.get())+"\n"
    str1+="Age: "+str(int(a1.get()))+"\n"
    str1+="Hobbies: "
    if c1.get()==1:
        str1+="Singing"
    if c2.get()==1:
        str1+="Reading"
    if c3.get()==1:
        str1+="Dancing"
    if r1.get()==1:
        str1+="\nGender: Male"
    else:
        str1+="\nGender: Female"
    m1=messagebox.showinfo("Details are: ",str1)

lbl1=Label(root,text="Username: ").grid(row=0,column=0)
e1=Entry(root,textvariable=name1).grid(row=0,column=1)

lbl2=Label(root,text="Email: ").grid(row=1,column=0)
e2=Entry(root,textvariable=email1).grid(row=1,column=1)

lbl3=Label(root,text="Select Age: ").grid(row=2,column=0)
age1=Scale(root,from_=15, to=55,orient=HORIZONTAL,variable=a1).grid(row=2,column=1,sticky="w")

lbl4=Label(root,text="Select Hobbies: ").grid(row=3,column=0)
h1=Checkbutton(root,text="Singing",variable=c1).grid(row=3,column=1,sticky="w")
h2=Checkbutton(root,text="Reading",variable=c2).grid(row=4,column=1,sticky="w")
h3=Checkbutton(root,text="Dancing",variable=c3).grid(row=5,column=1,sticky="w")

lbl5=Label(root,text="Select Gender: ").grid(row=6,column=0)
g1=Radiobutton(root,text="Male",variable=r1,value=1).grid(row=6,column=1, \
                                                          sticky="w")
g2=Radiobutton(root,text="Female",variable=r1,value=2).grid(row=7,column=1, \
                                                          sticky="w")
b1=Button(root,text="Submit",command=getDetails).grid(row=8,columnspan=2)
root.mainloop()










        
