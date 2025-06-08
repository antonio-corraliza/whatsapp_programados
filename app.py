
import pywhatkit
import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import sys
import os

# Función para obtener la ruta absoluta de un archivo de recurso
def resource_path(relative_path):
    """ Obtiene la ruta absoluta a un recurso, funciona para desarrollo y para PyInstaller """
    try:
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def max_caracter(P, numero_max):
    """
    Valida si la longitud de una cadena P es menor o igual a un número máximo dado.

    Args:
        P (str): La cadena a verificar.
        numero_max (str): La longitud máxima permitida como una cadena de texto.

    Returns:
        bool: True si la longitud de P es menor o igual a numero_max, False en caso contrario.
    """
    return len(P) <= int(numero_max)

def enviar_mensaje():
    """
    Envía un mensaje programado de WhatsApp a un solo destinatario.

    Valida el número de teléfono y la hora ingresados. Si son válidos, muestra un recordatorio
    para tener WhatsApp Web abierto y luego usa pywhatkit para enviar el mensaje a la
    hora especificada. Maneja posibles errores con cuadros de mensaje.
    """
    try:
        if telefono.get().isdigit() and len(telefono.get()) == 9 and len(hora.get()) == 4:
            messagebox.showinfo("Mensaje enviado!!!", "Recuerda tener abierta la sesion de WhatsApp en tu Navegador")
            pywhatkit.sendwhatmsg("+34" + telefono.get(), mensage.get("1.0", tk.END), 
                                int(hora.get()[0:2]), int(hora.get()[2:]),
                                wait_time=20, tab_close=True)
        else:
            messagebox.showerror("Error...", "Introduce un telefono correcto")                                          
    except:
        messagebox.showerror("Error...", "Introduce una hora y minutos correctos")

def multiple():
    """
    Abre una nueva ventana de Tkinter para enviar mensajes instantáneos de WhatsApp a múltiples destinatarios.

    Esta función gestiona la interfaz de usuario para añadir números de teléfono manualmente o desde un archivo CSV,
    mostrándolos en un listbox, y luego enviando un mensaje común a todos los números listados
    de forma instantánea. Incluye funciones para añadir números, cargar desde CSV y enviar.
    """
    def anadir_archivo():
        """
        Abre un cuadro de diálogo de archivo para seleccionar un archivo CSV y añade números de teléfono válidos de este
        al listbox para el envío de mensajes múltiples.

        Espera que los números de teléfono estén en la última columna del CSV y filtra los
        números de móvil españoles (que empiezan por '6' o '7') o números internacionales
        que empiezan por '+34' y luego '6' o '7'.
        """
        ruta_archivo = filedialog.askopenfilename(title="Seleccione un archivo", 
                                                  filetypes=[("Archivos csv", "*.csv")])
        if ruta_archivo:
            try:
                with open(ruta_archivo, "r") as archivo_csv:
                    contactos = csv.reader(archivo_csv)
                    for telefono in contactos:
                        if telefono[-1][0] in ("6","7"):
                            lista_num.insert(tk.END, telefono[-1].replace(" ",""))
                        elif telefono[-1][0] == "+":
                            if telefono[-1][3:][0] in ("6", "7"):
                                lista_num.insert(tk.END, telefono[-1][3:].replace(" ",""))
            except Exception as e:
                messagebox.showerror("Erorr", f"Algo fallo...{e}")
        
    def añadir():
        """
        Añade un número de teléfono introducido manualmente al listbox para el envío de mensajes múltiples.

        Valida que el número introducido sea una cadena de 9 dígitos antes de añadirlo.
        """
        if numeros.get().isdigit() and len(numeros.get()) == 9:
            lista_num.insert(tk.END, numeros.get())
            numeros.delete(0, tk.END)
        else:
            messagebox.showerror("error...", "Introduce numero valido")

    def envio_multi():
        """
        Envía el mensaje introducido instantáneamente a todos los números de teléfono en el listbox.

        Itera a través de la lista de números y usa pywhatkit para enviar un mensaje instantáneo
        a cada uno. Maneja posibles errores durante el proceso de envío.
        """
        messagebox.showinfo("Mensajes", f"Vas a enviar el mensaje a {len(lista_num.get(0, tk.END))} contactos")
        try:
            for numero in lista_num.get(0, tk.END):
                pywhatkit.sendwhatmsg_instantly("+34" + numero, texto_multi.get("1.0", tk.END))
        except Exception as e:
            messagebox.showerror("error", f"Algo fallo...{e}")
    
    root.destroy() # Cierra la ventana principal
    new_root = tk.Tk()
    new_root.title("Envio multiple numeros")
    new_root.geometry("530x840")
    new_root.resizable(False, False)
    # Usa la función resource_path para el icono
    icon_path = resource_path("WhatsApp.ico")
    new_root.iconbitmap(icon_path)

    limitador = (new_root.register(max_caracter), "%P", str(numero_caracteres))
     
    texto_numeros = tk.Label(new_root, text="Ingresa aqui los numeros de telefono")
    texto_numeros.grid(row=1, column=3)

    numeros = tk.Entry(new_root, width=9,
                       validate="key", validatecommand=limitador,
                       borderwidth=4)
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

    enviar = tk.Button(new_root, text="Enviar", 
                       width=10, command=envio_multi)
    enviar.grid(row=8, column=3)

    carga_archivo = tk.Button(new_root, text="Cargar archivo .csv",
                              command=anadir_archivo
                                 )
    carga_archivo.grid(row=9, column=3)
    
    new_root.mainloop()

    
root = tk.Tk()
root.title("WhatsApp Programados")
root.geometry("540x800")
root.resizable(False, False)
# Usa la función resource_path para el icono
icon_path = resource_path("WhatsApp.ico")
root.iconbitmap(icon_path)
messagebox.showinfo("Recordatorio","Recuerda mantener abierta tu sesion de WhatsApp en tu navegador!!!")
numero_caracteres = 9
limitador = (root.register(max_caracter), "%P", str(numero_caracteres))
caracteres_hora = 4
limitador_hora = (root.register(max_caracter), "%P", str(caracteres_hora))

texto = tk.Label(root, text="Envia tus WhatsApps a una hora programada!!!")
texto.grid(row=0, column=3)

texto_telefono = tk.Label(root, text="Telefono")
texto_telefono.grid(row=1, column=3)

telefono = tk.Entry(root, width=9,
                    validate="key", validatecommand=limitador,
                    borderwidth=4)
telefono.grid(row=2, column=3)

texto_mensaje = tk.Label(root, text="Mensaje")
texto_mensaje.grid(row=3, column=3)

mensage = tk.Text(root, width=40, height=20,
                  borderwidth=6)
mensage.grid(row=4, column=3)

texto_hora = tk.Label(root, text="Ingresa la hora con los minutos")
texto_hora.grid(row=5, column=3)

hora = tk.Entry(root, width=4,
                validate="key", validatecommand=limitador_hora,
                borderwidth=4)
hora.grid(row=6, column=3)

enviar = tk.Button(root, text="Enviar", command=enviar_mensaje, width=10)
enviar.grid(row=9, column=3)

texto_multiple = tk.Label(root, text="Tambien puedes enviar a multiples numeros de manera instantanea")
texto_multiple.grid(row=10, column=3)

boton_multiple = tk.Button(root, text="Envio multiple", 
                           width=15, height=2,
                           command=multiple)
boton_multiple.grid(row=11, column=3)

root.mainloop()