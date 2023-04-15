import smtplib
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Mail Application")
email_label = tk.Label(root, text="Email Address:")
email_label.grid(row=0, column=0)

email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

recipient_label = tk.Label(root, text="Recipient Email Address:")
recipient_label.grid(row=2, column=0)

recipient_entry = tk.Entry(root)
recipient_entry.grid(row=2, column=1)

subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=3, column=0)

subject_entry = tk.Entry(root)
subject_entry.grid(row=3, column=1)

message_label = tk.Label(root, text="Message:")
message_label.grid(row=4, column=0)

message_entry = tk.Text(root)
message_entry.grid(row=4, column=1)
def send_email():
    try:
        email = email_entry.get()
        password = password_entry.get()
        recipient = recipient_entry.get()
        subject = subject_entry.get()
        message = message_entry.get("1.0", tk.END)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)

        message = "Subject: {}\n\n{}".format(subject, message)
        server.sendmail(email, recipient, message)
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
send_button = tk.Button(root, text="Send", command=send_email)
send_button.grid(row=5, column=1)
root.mainloop()
