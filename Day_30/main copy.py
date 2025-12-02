import pandas as pd
import random
import os
from cryptography.fernet import Fernet
from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Import themed widgets

#  ENCRYPTION KEY - AUTO CREATE

def load_key():
    try:
        with open("key.key", "rb") as file:
            return file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("key.key", "wb") as file:
            file.write(key)
        return key

key = load_key()
fernet = Fernet(key)


#  PASSWORD GENERATOR

def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!#$%&()*+"

    nr_letters = random.randint(6, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(symbols) for _ in range(nr_symbols)] +
        [random.choice(numbers) for _ in range(nr_numbers)]
    )

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    window.clipboard_clear()
    window.clipboard_append(password)
    messagebox.showinfo("Copied!", "Password copied to clipboard.")


#  SAVE PASSWORD (ENCRYPTED)

def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not email or not password:
        messagebox.showerror("Error", "All fields are required.")
        return

    encrypted_password = fernet.encrypt(password.encode()).decode()

    def save_password():
        website = website_entry.get().strip()
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        if not website or not email or not password:
            messagebox.showerror("Error", "All fields are required.")
            return

        encrypted_password = fernet.encrypt(password.encode()).decode()

        new_data = {
            "website": website,
            "email": email,
            "password": encrypted_password
        }

        new_df = pd.DataFrame([new_data])

        if os.path.exists("passwords.csv"):
            # 1. Read existing data
            try:
                old_df = pd.read_csv("passwords.csv")

                # 2. Drop the old row if the website already exists (Case insensitive)
                clean_df = old_df[old_df["website"].str.lower() != website.lower()]

                # 3. Combine old (clean) data with the new entry
                final_df = pd.concat([clean_df, new_df], ignore_index=True)

            except pd.errors.EmptyDataError:
                # Handle case where file exists but is empty
                final_df = new_df
        else:
            # File doesn't exist yet
            final_df = new_df

        final_df.to_csv("passwords.csv", index=False)

        messagebox.showinfo("Saved", f"Password for {website} saved/updated successfully!")

        website_entry.delete(0, END)
        password_entry.delete(0, END)


#  SEARCH PASSWORD

def search_password():
    website = website_entry.get().strip()
    if not website:
        messagebox.showerror("Error", "Enter a website to search.")
        return

    if not os.path.exists("passwords.csv"):
        messagebox.showerror("Error", "No saved passwords found.")
        return

    df = pd.read_csv("passwords.csv")

    match = df[df['website'].str.lower() == website.lower()]

    if match.empty:
        messagebox.showerror("Not Found", f"No entry found for '{website}'.")
        return

    email = match.iloc[-1]["email"]
    encrypted_password = match.iloc[-1]["password"]
    decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()

    messagebox.showinfo(
        "Entry Found",
        f"Website: {website}\nEmail: {email}\nPassword: {decrypted_password}"
    )

    window.clipboard_clear()
    window.clipboard_append(decrypted_password)


#  SHOW/HIDE PASSWORD

def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="•")
        eye_button.config(text="👁")
    else:
        password_entry.config(show="")
        eye_button.config(text="🙈")


#  UI SETUP 

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="#f0f0f0") 

style = ttk.Style()
style.theme_use('clam')

LABEL_FONT = ("Arial", 10, "bold")
ENTRY_FONT = ("Arial", 11)

try:
    canvas = Canvas(height=200, width=200, bg="#f0f0f0", highlightthickness=0)
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1, pady=(0, 20))
except Exception:
    lbl_title = Label(window, text="🔑 Password Manager", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
    lbl_title.grid(row=0, column=0, columnspan=3, pady=(0, 20))


lbl_website = Label(window, text="Website:", font=LABEL_FONT, bg="#f0f0f0")
lbl_website.grid(row=1, column=0, sticky="e", padx=5, pady=5)

website_entry = ttk.Entry(window, width=35, font=ENTRY_FONT)
website_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
website_entry.focus()

btn_search = ttk.Button(window, text="Search", width=14, command=search_password)
btn_search.grid(row=1, column=2, padx=5, pady=5)


lbl_email = Label(window, text="Email/Username:", font=LABEL_FONT, bg="#f0f0f0")
lbl_email.grid(row=2, column=0, sticky="e", padx=5, pady=5)

email_entry = ttk.Entry(window, width=35, font=ENTRY_FONT)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
email_entry.insert(0, "example@email.com")


lbl_password = Label(window, text="Password:", font=LABEL_FONT, bg="#f0f0f0")
lbl_password.grid(row=3, column=0, sticky="e", padx=5, pady=5)

password_entry = ttk.Entry(window, width=21, font=ENTRY_FONT, show="•")
password_entry.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

btn_frame = Frame(window, bg="#f0f0f0")
btn_frame.grid(row=3, column=2, sticky="w")

eye_button = Button(btn_frame, text="👁", width=3, bg="white", relief="flat", command=toggle_password)
eye_button.pack(side="left", padx=5)

btn_generate = ttk.Button(btn_frame, text="Generate", width=10, command=generate_password)
btn_generate.pack(side="left")


btn_save = ttk.Button(window, text="Add to Password Manager", width=36, command=save_password)
btn_save.grid(row=4, column=1, columnspan=2, sticky="ew", pady=20, padx=5)


window.mainloop()