import tkinter as tk
from tkinter import messagebox

# Dummy user database
user_data = {}

# Switch to login screen
def go_to_login():
    register_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

# Switch to register screen
def go_to_register():
    login_frame.pack_forget()
    register_frame.pack(fill="both", expand=True)

# Registration function
def register_user():
    name = reg_name.get()
    age = reg_age.get()
    email = reg_email.get()
    password = reg_pass.get()
    gender = gender_var.get()

    if not all([name, age, email, password, gender]):
        messagebox.showwarning("Warning", "All fields are required.")
        return

    if email in user_data:
        messagebox.showerror("Error", "User already exists.")
        return

    user_data[email] = {"name": name, "age": age, "password": password, "gender": gender}
    messagebox.showinfo("Success", "Registration Successful!")
    reg_name.delete(0, tk.END)
    reg_age.delete(0, tk.END)
    reg_email.delete(0, tk.END)
    reg_pass.delete(0, tk.END)
    gender_var.set(None)
    go_to_login()

# Login function
def login_user():
    email = login_email.get()
    password = login_pass.get()

    if email in user_data and user_data[email]["password"] == password:
        messagebox.showinfo("Welcome", f"Welcome {user_data[email]['name']}!\nAge: {user_data[email]['age']}\nGender: {user_data[email]['gender']}")
    else:
        messagebox.showerror("Failed", "Invalid credentials.")

# Root window setup
root = tk.Tk()
root.title("Registration and Login Form")
root.geometry("400x500")
root.resizable(False, False)

# Aesthetic pastel color palette
PASTEL_BLUE = "#b3cde0"
PASTEL_PINK = "#fbb4ae"
PASTEL_PURPLE = "#decbe4"
PASTEL_GREEN = "#ccebc5"
PASTEL_YELLOW = "#fff2b2"
PASTEL_GRAY = "#f2f2f2"

# ---------- Register Frame ----------
register_frame = tk.Frame(root, bg=PASTEL_BLUE)

tk.Label(register_frame, text="Register", bg=PASTEL_PURPLE, fg="black", font=("Arial", 16, "bold"), relief="ridge", bd=2).pack(pady=10, fill="x", padx=20)

# Name
name_box = tk.LabelFrame(register_frame, text="Name", bg=PASTEL_GREEN, fg="black")
name_box.pack(fill="x", padx=20, pady=5)
reg_name = tk.Entry(name_box, bg=PASTEL_GRAY)
reg_name.pack(fill="x", padx=10, pady=5)

# Age
age_box = tk.LabelFrame(register_frame, text="Age", bg=PASTEL_YELLOW, fg="black")
age_box.pack(fill="x", padx=20, pady=5)
reg_age = tk.Entry(age_box, bg=PASTEL_GRAY)
reg_age.pack(fill="x", padx=10, pady=5)

# Email
email_box = tk.LabelFrame(register_frame, text="Email", bg=PASTEL_PINK, fg="black")
email_box.pack(fill="x", padx=20, pady=5)
reg_email = tk.Entry(email_box, bg=PASTEL_GRAY)
reg_email.pack(fill="x", padx=10, pady=5)

# Password
pass_box = tk.LabelFrame(register_frame, text="Password", bg=PASTEL_PURPLE, fg="black")
pass_box.pack(fill="x", padx=20, pady=5)
reg_pass = tk.Entry(pass_box, show="*", bg=PASTEL_GRAY)
reg_pass.pack(fill="x", padx=10, pady=5)

# Gender
gender_box = tk.LabelFrame(register_frame, text="Gender", bg=PASTEL_GREEN, fg="black")
gender_box.pack(fill="x", padx=20, pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(gender_box, text="Male", variable=gender_var, value="Male", bg=PASTEL_GREEN, fg="black").pack(side="left", padx=20)
tk.Radiobutton(gender_box, text="Female", variable=gender_var, value="Female", bg=PASTEL_GREEN, fg="black").pack(side="left")

# Register Button
tk.Button(register_frame, text="Register", command=register_user, bg=PASTEL_PURPLE, fg="black", font=("Arial", 12, "bold"), relief="groove").pack(pady=15)
tk.Button(register_frame, text="Already have an account? Login", command=go_to_login, bg=PASTEL_PINK, fg="black").pack()

# ---------- Login Frame ----------
login_frame = tk.Frame(root, bg=PASTEL_PINK)

tk.Label(login_frame, text="Login", bg=PASTEL_PURPLE, fg="black", font=("Arial", 16, "bold"), relief="ridge", bd=2).pack(pady=10, fill="x", padx=20)

# Email
login_email_box = tk.LabelFrame(login_frame, text="Email", bg=PASTEL_YELLOW, fg="black")
login_email_box.pack(fill="x", padx=20, pady=5)
login_email = tk.Entry(login_email_box, bg=PASTEL_GRAY)
login_email.pack(fill="x", padx=10, pady=5)

# Password
login_pass_box = tk.LabelFrame(login_frame, text="Password", bg=PASTEL_GREEN, fg="black")
login_pass_box.pack(fill="x", padx=20, pady=5)
login_pass = tk.Entry(login_pass_box, show="*", bg=PASTEL_GRAY)
login_pass.pack(fill="x", padx=10, pady=5)

tk.Button(login_frame, text="Login", command=login_user, bg=PASTEL_PURPLE, fg="black", font=("Arial", 12, "bold"), relief="groove").pack(pady=15)
tk.Button(login_frame, text="New user? Register", command=go_to_register, bg=PASTEL_BLUE, fg="black").pack()

# Start with Register screen
register_frame.pack(fill="both", expand=True)

root.mainloop()