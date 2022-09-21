from cgitb import text
import tkinter
window=tkinter.Tk()

#adding button widgets
btn=tkinter.Button(window, text="This is Button widget", fg='blue')
btn.pack()

#adding label widgets
lbl=tkinter.Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.pack()

#adding Textbox widgets
txtfld=tkinter.Entry(window, bd=5)
txtfld.insert(0,"This is Entry widget")

txtfld.pack()

window.title('Hello Python')
window.geometry("300x200")
window.mainloop()