
# GUI where the yellow grid will be the camera using open cv =)
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("TE App")

titulo = tk.Label(ventana, text="Live Inspection System")
titulo.grid(row=0, column=0, columnspan=4, sticky='ew')

for i in range(4):
    for j in range(4):
        label = tk.Label(ventana, text="")
        label.grid(row=i+1, column=j, padx=10, pady=10)


label_corte = tk.Label(ventana, text="Corte")
label_corte.grid(row=2, column=1)
label_corte_percentage = tk.Label(ventana, text="%")
label_corte_percentage.grid(row=2, column=2)

label_arranque = tk.Label(ventana, text="Arranque")
label_arranque.grid(row=3, column=1)
label_arranque_percentage = tk.Label(ventana, text="%")
label_arranque_percentage.grid(row=3, column=2)

# CAMERA!!
label_merged = tk.Label(ventana, text="Aquí irá la cámara", background="yellow")
label_merged.grid(row=2, column=3, rowspan=2, columnspan=2, sticky='nsew')

# RESIZING
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)
for i in range(1, 5):
    ventana.grid_columnconfigure(i, weight=1)
    ventana.grid_rowconfigure(i, weight=1)

ventana.mainloop()
