import tkinter as tk

root = tk.Tk()
root.title("Metodo pack()")

label1 = tk.Label(root, text="mi primer label", bg="red")
label2 = tk.Label(root, text="mi segundo label", bg="green")
label3 = tk.Label(root, text="mi tercer label", bg="blue")

label1.pack()
label2.pack(fill=tk.X)
label3.pack(side=tk.LEFT, fill=tk.Y)

root.mainloop()

