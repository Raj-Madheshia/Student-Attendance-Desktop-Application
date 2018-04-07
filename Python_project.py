from tkinter import *
from PIL import ImageTk,Image
R=Tk()
def new_class():
    new_class_frame = Tk()
    new_class_frame.resizable(width=FALSE, height=FALSE)
    new_class_frame.geometry('1000x600')
    new_class_frame.title('Create Class')
    Image_open=Image.open("newclass.jpg")
    image=ImageTk.PhotoImage(Image_open)
    logo=Label(new_class_frame,image=image)
    logo.place(x=0,y=0,bordermode="outside")

    def add():
        #----------- backend commands-----------------------



        #===================================================

        label_add = Label(new_class_frame,text="Added",bg="#566DEF",fg="#0F0")
        label_add.place(x=400,y=430)

    def home():
        new_class_frame.destroy()
        sec_frame()

    entry_name = Entry(new_class_frame,font=('arial',20,'bold'),width=17,bg="#E3E8B4",insertwidth=3)
    entry_name.place(x=400,y=178)

    entry_year = Entry(new_class_frame,font=('arial',20,'bold'),width=17,bg="#E3E8B4",insertwidth=3)
    entry_year.place(x=400,y=338)

    button_submit = Button(new_class_frame,text="ADD",width=9,height=2,fg="#000",bg="#E3E8B4",font=('arial',13,'bold'),activebackground='#10D234',command=add)
    button_submit.place(x=400,y=380)

    button_home = Button(new_class_frame, text="HOME",width=9,height=2,fg="#000",bg="#E3E8B4",font=('arial',13,'bold'),activebackground='#566DEF',command=home)
    button_home.place(x=900,y=100)
    new_class_frame.mainloop()

    
def studentReport():
    studentReport_frame = Tk()
    studentReport_frame.resizable(width=FALSE, height=FALSE)
    studentReport_frame.geometry('1000x600')
    

    studentReport_frame.title('Create Class')
    Image_open=Image.open("report.jpg")
    image=ImageTk.PhotoImage(Image_open)
    logo=Label(studentReport_frame,image=image)
    logo.place(x=0,y=0,bordermode="outside")
    def home():
        studentReport_frame.destroy()
        sec_frame()
    
    def search():
        #-------------------database work----------------------
        pass
    button_search = Button(studentReport_frame, text="SEARCH",width=8,height=1,fg="#000",bg="#566DEF",font=('arial',13,'bold'),activebackground='#566DEF',command=search)
    button_search.place(x=800,y=13)

    button_home = Button(studentReport_frame, text="HOME",width=6,height=1,fg="#000",bg="#566DEF",font=('arial',13,'bold'),activebackground='#566DEF',command=home)
    button_home.place(x=890,y=13)
    studentReport_frame.mainloop()

def newAttendance():
    newAttendance_frame = Tk()
    newAttendance_frame.resizable(width=FALSE, height=FALSE)
    newAttendance_frame.geometry('1000x600')
    newAttendance_frame.title('New Attendance')
    Image_open=Image.open("newAttendance.jpg")
    image=ImageTk.PhotoImage(Image_open)
    logo=Label(newAttendance_frame,image=image)
    logo.place(x=0,y=0,bordermode="outside")

    def new_add():
        pass

    def home():
        newAttendance_frame.destroy()
        sec_frame()
    entry_total = Entry(newAttendance_frame,font=('arial',20,'bold'),width=6,bg="#E3E8B4",insertwidth=2)
    entry_total.place(x=437,y=308)

    entry_atten = Entry(newAttendance_frame,font=('arial',20,'bold'),width=6,bg="#E3E8B4",insertwidth=2)
    entry_atten.place(x=730,y=308)

    button_add = Button(newAttendance_frame,text="ADD",width=9,height=2,fg="#000",bg="#E3E8B4",font=('arial',13,'bold'),activebackground='#566DEF',command=new_add)
    button_add.place(x=730,y=380)

    button_home = Button(newAttendance_frame, text="HOME",width=9,height=2,fg="#000",bg="#E3E8B4",font=('arial',13,'bold'),activebackground='#566DEF',command=home)
    button_home.place(x=910,y=135)
    newAttendance_frame.mainloop()

def newStudent():
    newStudent_frame = Tk()
    newStudent_frame.resizable(width=FALSE, height=FALSE)
    newStudent_frame.geometry('1000x600')
    newStudent_frame.title('Student Entry')
    Image_open=Image.open("newStudent.jpg")
    image=ImageTk.PhotoImage(Image_open)
    logo=Label(newStudent_frame,image=image)
    logo.place(x=0,y=0,bordermode="outside")

    Image_open1=Image.open("vesit.png")
    image1=ImageTk.PhotoImage(Image_open1)
    logo1=Label(newStudent_frame,image=image1)
    logo1.place(x=200,y=200,bordermode="outside")

    def new_add():
        pass
    def home():
        newStudent_frame.destroy()
        sec_frame()
    entry_fname = Entry(newStudent_frame,font=('arial',20,'bold'),width=16,bg="#E3E8B4",insertwidth=2)
    entry_fname.place(x=730,y=293)
    entry_grno = Entry(newStudent_frame,font=('arial',20,'bold'),width=16,bg="#E3E8B4",insertwidth=2)
    entry_grno.place(x=730,y=215)

    entry_class = Entry(newStudent_frame,font=('arial',20,'bold'),width=16,bg="#E3E8B4",insertwidth=2)
    entry_class.place(x=730,y=368)

    entry_roll = Entry(newStudent_frame,font=('arial',20,'bold'),width=16,bg="#E3E8B4",insertwidth=2)
    entry_roll.place(x=730,y=435)

    button_add = Button(newStudent_frame,text="ADD",width=9,height=2,fg="#000",bg="#E3E8B4",font=('arial',13,'bold'),activebackground='#566DEF',command=new_add)
    button_add.place(x=730,y=500)

    button_home = Button(newStudent_frame, text="HOME",width=9,height=3,fg="#000",bg="#566DEF",font=('arial',13,'bold'),activebackground='#566DEF',command=home)
    button_home.place(x=910,y=64)
    newStudent_frame.mainloop()
    

#--------------------------------SECOND FRAME-------------------------------------------
def sec_frame():
    sec = Tk()
    sec.resizable(width=FALSE, height=FALSE)
    sec.geometry('1000x600')
    sec.title('Report')
    Image_open=Image.open("different_field.jpg")
    image=ImageTk.PhotoImage(Image_open)
    logo=Label(sec,image=image)
    logo.place(x=0,y=0,bordermode="outside")
    button_s_r = Button(sec,text="STUDENT AND REPORT",width=34,height=16,bg="#E3E7B4",command=lambda:function(1))
    button_s_r.place(x=217,y=32)
    
    button_new_attendance = Button(sec,text="NEW ATTENDANCE",width=34,height=16,bg="#E3E7B4",command=lambda:function(2))
    button_new_attendance.place(x=554,y=32)

    button_new_student = Button(sec,text="NEW STUDENT",width=34,height=16,bg="#E3E7B4",command=lambda:function(3))
    button_new_student.place(x=217,y=324)

    button_new_class = Button(sec,text="CREATE NEW CLASS",width=34,height=16,bg="#E3E7B4",command=lambda:function(4))
    button_new_class.place(x=554,y=324)

    def function(value):
        if(value==4):
            sec.destroy()
            new_class()
        elif(value==2):
            sec.destroy()
            newAttendance()
        elif(value==3):
            sec.destroy()
            newStudent()
        elif(value==1):
            sec.destroy()
            studentReport()
    
    sec.mainloop()


#-----------------------------------FIRST FRAME------------------------------------------    
def main_frame():
    def login_click():
        R.destroy()
        sec_frame()
    #login_label = Label(R,text="login")
    #login_label.place(x=700,y=225)

    entry_username = Entry(R,font=('arial',20,'bold'),width=13,bg="#E3E8B4",insertwidth=3)
    entry_username.place(x=700,y=225)

    entry_password = Entry(R,font=('arial',20,'bold'),show="*",width=13,bg="#E3E8B4",insertwidth=3)
    entry_password.place(x=700,y=330)

    login= Button(R,text="SIGN IN",fg="#FFF",bg="#566DEF",width=31,height=2,font=('arial',13,'bold'),
                  activebackground='#10D234',command=login_click)
    login.place(x=615,y=420)

    

R.resizable(width=FALSE, height=FALSE)
R.geometry('1000x600')
R.title('Sign up')
Image_open=Image.open("bgimage.jpg")
image=ImageTk.PhotoImage(Image_open)
logo=Label(R,image=image)
logo.place(x=0,y=0,bordermode="outside")
main_frame()



R.mainloop()
