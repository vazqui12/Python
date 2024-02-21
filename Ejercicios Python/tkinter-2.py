import tkinter as tk

root = tk.Tk()
root.title("Metodo pack()")

label1 = tk.Label(root, text="mi primer label", bg="red")
label2 = tk.Label(root, text="mi segundo label", bg="green")
label3 = tk.Label(root, text="mi primer label", bg="blue")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2)

root.mainloop()

