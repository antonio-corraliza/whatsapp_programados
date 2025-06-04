
import pywhatkit
import tkinter as tk
from tkinter import messagebox

def max_caracter(P, numero_max):
    return len(P) <= int(numero_max)

def enviar_mensaje():
    try:
        if telefono.get().isdigit() and len(telefono.get()) == 9 and len(hora.get()) == 4:
            messagebox.showinfo("Mensaje enviado!!!", "Recuerda tener abierta la sesion de WhatsApp en tu Navegador")
            pywhatkit.sendwhatmsg("+34" + telefono.get(), mensage.get("1.0", tk.END), 
                                int(hora.get()[0:2]), int(hora.get()[2:]),
                                wait_time=10, tab_close=True)
        else:
            messagebox.showerror("Error...", "Introduce un telefono correcto")                                          
    except:
        messagebox.showerror("Error...", "Introduce una hora y minutos correctos")

def multiple():
    def añadir():
        if numeros.get().isdigit() and len(numeros.get()) == 9:
            lista_num.insert(tk.END, numeros.get())
            numeros.delete(0, tk.END)
        else:
            messagebox.showerror("error...", "Introduce numero valido")

    def envio_multi():
        try:
            for numero in lista_num.get(0, tk.END):
                pywhatkit.sendwhatmsg_instantly("+34" + numero, texto_multi.get("1.0", tk.END))
        except Exception as e:
            messagebox.showerror("error", f"Algo fallo...{e}")
    
    root.destroy()
    new_root = tk.Tk()
    new_root.title("Envio multiple")
    new_root.geometry("530x800")
    limitador = (new_root.register(max_caracter), "%P", str(numero_caracteres))
     
    texto_numeros = tk.Label(new_root, text="Ingresa aqui los numeros de telefono")
    texto_numeros.grid(row=1, column=3)

    numeros = tk.Entry(new_root, width=9,
                       validate="key", validatecommand=limitador)
    numeros.grid(row=2, column=3)
    
    mostrar_num = tk.Button(new_root, text="Ingresar", command=añadir)
    mostrar_num.grid(row=3, column=3)

    lista_num = tk.Listbox(new_root, width=12, height=4)
    lista_num.grid(row=4, column=3)

    eliminar = tk.Button(new_root, text="Eliminar",
                        command=lambda:lista_num.delete(tk.ACTIVE)                    
                         )
    eliminar.grid(row=5, column=3)

    texto_mensaje_mul = tk.Label(new_root, text="Mensaje")
    texto_mensaje_mul.grid(row=6, column=3)

    texto_multi = tk.Text(new_root, width=40, height=20,
                          borderwidth=6)
    texto_multi.grid(row=7, column=3)

    enviar = tk.Button(new_root, text="Envio multiple", command=envio_multi)
    enviar.grid(row=8, column=3)
    
    new_root.mainloop()

    
root = tk.Tk()
root.title("WhatsApp Programados")
root.geometry("530x800")
numero_caracteres = 9
limitador = (root.register(max_caracter), "%P", str(numero_caracteres))
caracteres_hora = 4
limitador_hora = (root.register(max_caracter), "%P", str(caracteres_hora))

texto = tk.Label(root, text="Envia tus WhatsApps a una hora programada!!!")
texto.grid(row=0, column=3)

texto_telefono = tk.Label(root, text="Telefono")
texto_telefono.grid(row=1, column=3)

telefono = tk.Entry(root, width=9,
                    validate="key", validatecommand=limitador)
telefono.grid(row=2, column=3)

texto_mensaje = tk.Label(root, text="Mensaje")
texto_mensaje.grid(row=3, column=3)

mensage = tk.Text(root, width=40, height=20,
                  borderwidth=6)
mensage.grid(row=4, column=3)

texto_hora = tk.Label(root, text="Ingresa la hora con los minutos")
texto_hora.grid(row=5, column=3)

hora = tk.Entry(root, width=4,
                validate="key", validatecommand=limitador_hora)
hora.grid(row=6, column=3)

enviar = tk.Button(root, text="Enviar", command=enviar_mensaje, width=10)
enviar.grid(row=9, column=3)

texto_multiple = tk.Label(root, text="Tambien puedes enviar multiples mensajes de manera instantanea")
texto_multiple.grid(row=10, column=3)

boton_multiple = tk.Button(root, text="Envio multiple", 
                           width=15, height=2,
                           command=multiple)
boton_multiple.grid(row=11, column=3)

root.mainloop()