from tkinter import*

def miles_to_km():
    miles_to_convert = float(miles.get())
    km = round(miles_to_convert * 1.609)
    kilometer.config(text=f"{km}")
    
window = Tk()


window.title("Miles to Kilometer Converter")
window.config(padx=40, pady=40)

miles = Entry(width=10)
miles.grid(column= 1, row= 0)

miles_label = Label(text="Miles")
miles_label.grid(column= 2,row=0)

kilometer = Label(text="0")
kilometer.grid(column=1,row=1)

kilometer_label = Label(text="Km")

kilometer_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()