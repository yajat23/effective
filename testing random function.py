from tkinter import *
import random

root = Tk()
root.title("Testing Random Function")
root.geometry("500x500")
root.configure(background = "red")

input_password = Entry(root)
guessed_password_label = Label(root)
generated_password_label = Label(root)

array_3d = [[["1", "2", "3", "4", "5", "6", "I", "J", "K", "L", "M", "N", "O", "P"], ["Head", "Tail", "King", "Queen"], ["A", "B", "C", "D", "E", "F", "G", "H", "!", "@", "#", "$", "%", "^", "&", "*"]]]
print(array_3d[0][2][3])

def new_password():
    random_no1 = random.randint(0, 13)
    random_no2 = random.randint(0, 3)
    random_no3 = random.randint(0, 15)
    
    letter1 = array_3d[0][0][random_no1]
    letter2 = array_3d[0][1][random_no2]
    letter3 = array_3d[0][2][random_no3]
    
    guessed_password_label["text"] = "Guessed Password : " + input_password.get()
    generated_password_label["text"] = "Generated Password : " + letter1 + "" + letter2 + "" + letter3
    
btn = Button(root, text = "New Password", command = new_password)

input_password.place(relx = 0.5, rely = 0.3, anchor = CENTER)
guessed_password_label.place(relx = 0.5, rely = 0.4, anchor = CENTER)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
generated_password_label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()