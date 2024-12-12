from tkinter import *

window = Tk()
window.minsize(width=250,height=150)
window.config(padx=30,pady=30)
window.title("BMI Calculator")

#height
label_height = Label(text="Enter Your Height(cm)",padx=5)
label_height.pack()
entry_height = Entry(width=10)
entry_height.pack()

#weight
label_weight = Label(text="Enter Your Weight(kg)",padx=5)
label_weight.pack()
entry_weight = Entry(width=10)
entry_weight.pack()

# result
result_label = Label(text="", padx=5)
result_label.pack()
result_bmi = Label(text="",padx=5)
result_bmi.pack()


#calculate
def calculate():
    try:
        height_cm = float(entry_height.get())
        weight_kg = float(entry_weight.get())

        height_m = height_cm / 100

        bmi = weight_kg / (height_m ** 2)

        if bmi < 18.5:
            result = "Düşük Kilolu"
        elif 18.5 <= bmi < 24.99:
            result = "Normal Kilo"
        elif 25.0 <= bmi < 29.99:
            result = "Fazla Kilolu"
        else:
            result = "Obez"

        # Display result
        result_bmi.config(text=round(bmi))
        result_label.config(text=result)

    except ValueError:
        result_label.config(text="Please enter valid numbers.")


calculate_button = Button(text="Calculate",width=10,command=calculate)
calculate_button.config(padx=5)
calculate_button.pack()



window.mainloop()


