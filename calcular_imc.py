# imc = peso / altura **2

import tkinter as tk

def calcular_imc():
    peso = float(entry1.get())
    altura = float(entry2.get())
    imc = peso / altura **2
    result.config(text=f'IMC:%d'% (imc))

root = tk.Tk()
root.title('DESCUBRA SEU IMC , CLIQUE AQUI ! ')
root.geometry('400x500')

label1 = tk.Label(root, text='Peso:')
label1.pack()

entry1 = tk.Entry(root, bg='yellow')
entry1.pack()

label3 = tk.Label(root, text=' ')
label3.pack()

label2 = tk.Label(root, text='Altura:')
label2.pack()

entry2 = tk.Entry(root, bg='yellow')
entry2.pack()

label3 = tk.Label(root, text=' ')
label3.pack()

btn_imc = tk.Button(root, text='IMC', width = 20, fg='white', bg='#000000', command = calcular_imc)
btn_imc.pack()

result = tk.Label(root, text='seu IMC é :')
result.pack()

root.mainloop()
    

