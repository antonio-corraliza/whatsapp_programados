
import pywhatkit
import tkinter as tk
from tkinter import messagebox

def enviar():
    try:
        if telefono.get().isdigit() and len(telefono.get()) == 9:
            messagebox.showinfo("Mensaje enviado!!!", "Recuerda tener abierta la sesion de WhatsApp en tu Navegador")
            pywhatkit.sendwhatmsg("+34" + telefono.get(), mensage.get("1.0", tk.END), 
                                int(hora.get()), int(minuto.get()),
                                wait_time=10, tab_close=True)
        else:
            messagebox.showinfo("Error...", "Introduce un telefono correcto")                                          
    except:
        messagebox.showinfo("Error...", "Introduce una hora y minutos correctos")

root = tk.Tk()
root.title("WhatsApp Programados")

texto = tk.Label(root, text="Envia tus WhatsApps a una hora programada!!!")
texto.grid(row=0, column=3)

texto_telefono = tk.Label(root, text="Telefono")
texto_telefono.grid(row=1, column=3)

telefono = tk.Entry(root, width=9)
telefono.grid(row=2, column=3)

texto_mensaje = tk.Label(root, text="Mensaje")
texto_mensaje.grid(row=3, column=3)

mensage = tk.Text(root, width=50)
mensage.grid(row=4, column=3)

texto_hora = tk.Label(root, text="Hora")
texto_hora.grid(row=5, column=3)

hora = tk.Entry(root, width=2)
hora.grid(row=6, column=3)

texto_minutos = tk.Label(root, text="Minuto")
texto_minutos.grid(row=7, column=3)

minuto = tk.Entry(root, width=2)
minuto.grid(row=8, column=3)

enviar = tk.Button(root, text="Enviar", command=enviar,
                   width=6, height=2
                   )
enviar.grid(row=9, column=3)


root.mainloop()