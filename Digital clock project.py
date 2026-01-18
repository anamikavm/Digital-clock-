#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from time import strftime
from datetime import datetime

def update_clock():
    time_string = strftime('%H:%M:%S')
    date_string = datetime.now().strftime('%d-%m-%Y')
    clock_label.config(text=time_string)
    date_label.config(text="Date: " + date_string)
    root.after(1000, update_clock)

# Set up window
root = tk.Tk()
root.title("Indian Railways Digital Clock")
root.geometry("400x200")
root.configure(bg='black')

# Time Display
clock_label = tk.Label(root, font=('Helvetica', 48, 'bold'), bg='black', fg='lime')
clock_label.pack(pady=10)

# Date Display
date_label = tk.Label(root, font=('Helvetica', 18), bg='black', fg='yellow')
date_label.pack()

# Station Info
station_label = tk.Label(root, text="Station: New Delhi (NDLS)", font=('Arial', 14), bg='black', fg='white')
station_label.pack()

# Train Info
train_label = tk.Label(root, text="Train No: 12345 Rajdhani Express", font=('Arial', 14), bg='black', fg='white')
train_label.pack(pady=5)

update_clock()
root.mainloop()


# In[1]:


# In[ ]:




