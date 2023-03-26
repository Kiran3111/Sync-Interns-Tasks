import os
import math
import random
import smtplib
import tkinter as tk

window = tk.Tk()
window.title("OTP Verification")
window.geometry("400x250")

email_label = tk.Label(text="Enter your email:")
email_label.pack(pady=10)
email_entry = tk.Entry(width=30)
email_entry.pack()

OTP = ""

def send_otp():
    global OTP
    
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"
    msg= otp
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("gladingiop3111@gmail.com", "mxzpxothslvwotdm")
    emailid = email_entry.get()
    s.sendmail('&&&&&&&&&&&',emailid,msg)
    s.quit()
    
    otp_entry.config(state='normal')
    send_otp_button.config(state='disabled')
    email_entry.config(state='disabled')
    
    if otp_entry.get() != '':
        verify_button.config(state='normal')

otp_button = tk.Button(text="Send OTP", command=send_otp)
otp_button.pack(pady=10)

otp_entry_label = tk.Label(text="Enter Your OTP:")
otp_entry_label.pack()
otp_entry = tk.Entry(width=30, state='disabled')
otp_entry.pack()

def verify_otp():
    entered_otp = otp_entry.get()
    if entered_otp == OTP:
        result_label.config(text="Verified", fg='green')
    else:
        result_label.config(text="Please Check your OTP again", fg='red')

verify_button = tk.Button(text="Verify OTP", command=verify_otp, state='disabled')
verify_button.pack(pady=10)

result_label = tk.Label(text="")
result_label.pack()

def enable_verify_button(*args):
    if otp_entry.get() != '':
        verify_button.config(state='normal')
    else:
        verify_button.config(state='disabled')
otp_entry_var = tk.StringVar()
otp_entry.config(textvariable=otp_entry_var)
otp_entry_var.trace_add('write', enable_verify_button)

window.mainloop()
