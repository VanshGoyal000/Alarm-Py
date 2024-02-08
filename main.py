from datetime import datetime
import tkinter as tk
from tkinter import simpledialog

window = tk.tk()
window.title("Its time")
window.geometry("300x200")


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


x = input("in format  'hh:mm:ss'")
h_target , m_target , s_target = map(int , x.split(':') )


while True:
    # Get the current time
    current_time = datetime.now().strftime("%H:%M:%S")
    h, m, s = map(int, current_time.split(':'))
    
    # Check if the current time reaches or surpasses the target time
    if (h == h_target and m == m_target and s >= s_target):
        print("hogya")
        break
    





# h, m = map(int, x.split(':'))

# t = h*



# while(True):

#     if current_time == x :
#         print("Time is up")
#         break
