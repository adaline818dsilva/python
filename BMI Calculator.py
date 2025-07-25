import tkinter
def blink():
    current_color = res.cget("fg")
    next_color = "red" if current_color == "blue" else "blue"
    res.config(fg=next_color)
    res.after(500, blink)

def cal_bmi():
    h = float(ht_value.get())
    w = float(wt_val.get())
    h1 = h / 100
    bmi = w / (h1 ** 2)

    if bmi < 18.5:
        status = "underweight"
    elif 18.5 <= bmi <= 24.9:
        status = "normal weight"
    else:
        status = "obesity"

    res.config(text=f"BMI IS {bmi:.2f} ({status})", bg="white", fg="blue")
    blink()

root = tkinter.Tk()
root.geometry("500x500")
root.title("BMI Calculator")
root.config(bg="pink")

head = tkinter.Label(root, text="BMI CALCULATOR", font=("Arial", 20, "bold"), bg="pink",fg="black")
head.pack(pady=20)

fr = tkinter.Frame(root, bg="pink")
fr.pack(pady=10)


ht = tkinter.Label(fr, text="HEIGHT (in cm)", font=("Arial", 15), bg="pink")
ht.grid(row=0, column=0, padx=5, pady=5)
ht_value = tkinter.Entry(fr)
ht_value.grid(row=0, column=1, padx=5, pady=5)


wt = tkinter.Label(fr, text="WEIGHT (in kg)", font=("Arial", 15), bg="pink")
wt.grid(row=1, column=0, padx=5, pady=5)
wt_val = tkinter.Entry(fr)
wt_val.grid(row=1, column=1, padx=5, pady=5)


bt = tkinter.Button(root, text="Calculate", font=("Arial", 20, "bold"), fg="purple", bg="yellow", command=cal_bmi)
bt.pack(pady=20)


res = tkinter.Label(root, text="", font=("Arial", 20, "bold"), bg="white")
res.pack(pady=20)

root.mainloop()
