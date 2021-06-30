from tkinter import * 

root = Tk()
root.geometry('600x600')
root.title("Registration Form")
root.configure(background=input("Choose the colour: "))


Fullname=StringVar()
Email=StringVar()
var = IntVar()
x=StringVar()
y=StringVar()
var1= IntVar()



def form():

   print("FullName: ", Fullname.get())    
   print("EmailID: ", Email.get())
   print("Country: ",x.get())
   print("Course: ",y.get())
   return


   
   
             
a = Label(root, text="Registration form",width=20,bg="Red", fg="black",font="Verdana 16 bold italic")
a.place(x=60,y=53)


b = Label(root, text="FullName",width=20,font=("bold", 10))
b.place(x=60,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

c = Label(root, text="Email",width=20,font=("bold", 10))
c.place(x=60,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)




d = Label(root, text="Gender",width=20,font=("bold", 10))
d.place(x=60,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=60,y=280)

list1 = ['India','UK','USA','South Africa','Other'];

droplist=OptionMenu(root,x, *list1)
droplist.config(width=15)
x.set('select your country') 
droplist.place(x=240,y=280)

label_5 = Label(root, text="Course",width=20,font=("bold", 10))
label_5.place(x=60,y=330)

list2 = ['AI','ML','IoT','IR4']

droplist1=OptionMenu(root,y, *list2)
droplist1.config(width=15)
y.set('select your Course') 
droplist1.place(x=240,y=330)
var2= IntVar()


Button(root, text='Submit',width=20,bg='brown',fg='white',command=form).place(x=180,y=380)

root.mainloop()






























