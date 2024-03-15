from tkinter import *
from tkinter import ttk, messagebox
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    label_time.config(text=current_time)
    label_time.after(1000, update_time)

def show_thankyou(message):
    messagebox.showinfo("Thank You", message + " ❤️")

def submit_girls():
    name = entry_name_girls.get()
    contact = entry_contact_girls.get()
    selected_service = services_var_girls.get()
    selected_time = time_var_girls.get()
    message = f"Thank you, {name}!\nYou have selected {selected_service} and your appointment is scheduled for {selected_time}."
    show_thankyou(message)
    button_submit_girls.config(state=DISABLED)

def submit_boys():
    name = entry_name_boys.get()
    contact = entry_contact_boys.get()
    selected_service = services_var_boys.get()
    selected_time = time_var_boys.get()
    message = f"Thank you, {name}!\nYou have selected {selected_service} and your appointment is scheduled for {selected_time}."
    show_thankyou(message)
    button_submit_boys.config(state=DISABLED)

win = Tk()
win.title("Aastha's Salon")
win.geometry("800x500")
win.configure(bg='#FFC0CB')  

heading_font = ('Verdana', 20, 'bold')
label_heading = Label(win, text="We’ll style while you smile‪‪❤︎‬\nRevitalize your beauty, Revitalize your soul in Aastha's Salon !!", font=heading_font, bg='#FFC0CB')
label_heading.pack(pady=20)

frame_girls = Frame(win, bg='#DBB9D2', bd=2, relief=SOLID)
frame_girls.place(relx=0.25, rely=0.5, anchor=CENTER)

label_section_girls = Label(frame_girls, text='Girls Section', font=('Arial', 16, 'bold'), bg='#DBB9D2', fg='white')
label_section_girls.pack(pady=10)

label1_girls = Label(frame_girls, text='Name:', font=('Arial', 14), bg='#DBB9D2')
label1_girls.pack(pady=10)

entry_name_girls = Entry(frame_girls, font=('Arial', 14))
entry_name_girls.pack(pady=10)

label2_girls = Label(frame_girls, text='Contact Number:', font=('Arial', 14), bg='#DBB9D2')
label2_girls.pack(pady=10)

entry_contact_girls = Entry(frame_girls, font=('Arial', 14))
entry_contact_girls.pack(pady=10)

label3_girls = Label(frame_girls, text='Select Services:', font=('Arial', 14), bg='#DBB9D2')
label3_girls.pack(pady=10)

services_girls = ["Manicures - 1000 rs", "Pedicures - 1300 rs", "Facial Treatments - 5000 rs", "Hair Care - 2700 rs", "Body Massage - 6000 rs"]
services_var_girls = StringVar()
services_dropdown_girls = ttk.Combobox(frame_girls, textvariable=services_var_girls, values=services_girls, font=('Arial', 14))
services_dropdown_girls.pack(pady=10)

label4_girls = Label(frame_girls, text='Select Time:', font=('Arial', 14), bg='#DBB9D2')
label4_girls.pack(pady=10)

time_options_girls = ["Morning 9 am - 11 am", "Afternoon 2 pm - 4 pm", "Evening 7 pm - 9 pm"]
time_var_girls = StringVar()
time_dropdown_girls = ttk.Combobox(frame_girls, textvariable=time_var_girls, values=time_options_girls, font=('Arial', 14))
time_dropdown_girls.pack(pady=10)

button_submit_girls = Button(frame_girls, text="Submit", command=submit_girls, font=('Arial', 16))
button_submit_girls.pack(pady=20)

frame_boys = Frame(win, bg='#DBB9D2', bd=2, relief=SOLID)
frame_boys.place(relx=0.75, rely=0.5, anchor=CENTER)

label_section_boys = Label(frame_boys, text='Boys Section', font=('Arial', 16, 'bold'), bg='#DBB9D2', fg='white')
label_section_boys.pack(pady=10)

label1_boys = Label(frame_boys, text='Name:', font=('Arial', 14), bg='#DBB9D2')
label1_boys.pack(pady=10)

entry_name_boys = Entry(frame_boys, font=('Arial', 14))
entry_name_boys.pack(pady=10)

label2_boys = Label(frame_boys, text='Contact Number:', font=('Arial', 14), bg='#DBB9D2')
label2_boys.pack(pady=10)

entry_contact_boys = Entry(frame_boys, font=('Arial', 14))
entry_contact_boys.pack(pady=10)

label3_boys = Label(frame_boys, text='Select Services:', font=('Arial', 14), bg='#DBB9D2')
label3_boys.pack(pady=10)

services_boys = ["Haircut - 450 rs", "Hair Colour - 800 rs", "Shave - 300 rs", "Beard Trim - 200 rs", "Beard Colour - 700 rs", "Head Massage - 1000 rs", "Body Massage - 3000 rs"]
services_var_boys = StringVar()
services_dropdown_boys = ttk.Combobox(frame_boys, textvariable=services_var_boys, values=services_boys, font=('Arial', 14))
services_dropdown_boys.pack(pady=10)

label4_boys = Label(frame_boys, text='Select Time:', font=('Arial', 14), bg='#DBB9D2')
label4_boys.pack(pady=10)

time_options_boys = ["Morning 9 am - 11 am", "Afternoon 2 pm - 4 pm", "Evening 7 pm - 9 pm"]
time_var_boys = StringVar()
time_dropdown_boys = ttk.Combobox(frame_boys, textvariable=time_var_boys, values=time_options_boys, font=('Arial', 14))
time_dropdown_boys.pack(pady=10)

button_submit_boys = Button(frame_boys, text="Submit", command=submit_boys, font=('Arial', 16))
button_submit_boys.pack(pady=20)

label_time = Label(win, font=('Arial', 20, 'italic', 'bold'), fg='black', bg='#FFC0CB', anchor='e')
label_time.pack(side=BOTTOM, fill=X, padx=10, pady=10)

update_time()

win.mainloop()