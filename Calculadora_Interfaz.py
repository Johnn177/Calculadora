import tkinter as tk
root = tk.Tk()
num_uno = tk.StringVar()
num_dos= tk.StringVar()
resultado = tk.StringVar()
def suma():
    a=int(num_uno.get())
    b=int(num_dos.get())
    resultado.set(a+b)
def resta():
    a = int(num_uno.get())
    b = int(num_dos.get())
    resultado.set(a - b)
def mul():
    a = int(num_uno.get())
    b = int(num_dos.get())
    resultado.set(a * b)
def div():
    a = int(num_uno.get())
    b = int(num_dos.get())
    resultado.set(a / b)
root.geometry('420x160')
root.title('Calculadora')
root.configure(bg="#009688")
tk.Label(root, text='Primer Numero: ', bg="#009688", fg='white', font=('', 12)).place(x=30, y=10)
tk.Entry(root, justify='center', textvariable=num_uno).place(x=250, y=10)
tk.Label(root, text='Segundo Numero: ', bg="#009688", fg='white', font=('', 12)).place(x=30, y=40)
tk.Entry(root, justify='center', textvariable=num_dos).place(x=250, y=40)
tk.Button(root, text='Suma', bd=0, command=suma).place(x=65, y=80)
tk.Button(root, text='Resta', bd=0, command=resta).place(x=125, y=80)
tk.Button(root, text='Multiplicación', bd=0, command=mul).place(x=185, y=80)
tk.Button(root, text='División', bd=0, command=div).place(x=290, y=80)
tk.Label(root, textvariable=resultado, bg="#009688", fg='white', font=('', 12)).place(x=200, y=120)
root.mainloop()