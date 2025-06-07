Aplicación de Envío de Mensajes de WhatsApp
Esta es una aplicación de escritorio desarrollada con tkinter en Python que permite enviar mensajes de WhatsApp de dos maneras:

Programados: Envía un mensaje a un solo número de teléfono a una hora específica.

Múltiples/Instantáneos: Envía un mensaje a varios números de teléfono de forma instantánea, con la opción de cargar los números desde un archivo CSV o introducirlos manualmente.

Características
Envío de mensajes programados a un número individual.

Envío instantáneo de mensajes a múltiples números.

Validación de formato de número de teléfono y hora.

Carga de números de teléfono desde archivos .csv.

Interfaz de usuario intuitiva con tkinter.

Requisitos
Para ejecutar esta aplicación, necesitas tener instaladas las siguientes librerías de Python:

pywhatkit

tkinter (normalmente viene incluido con Python)

csv (normalmente viene incluido con Python)

Puedes instalar pywhatkit usando pip:

pip install pywhatkit

Cómo Usar
1. Envío de Mensajes Programados (Ventana Principal)
Número de Teléfono: En el campo "Telefono", introduce el número de WhatsApp (solo 9 dígitos, sin el prefijo de país). La aplicación añadirá automáticamente el prefijo +34.

Mensaje: Escribe el mensaje que deseas enviar en el área de texto "Mensaje".

Hora: En el campo "Ingresa la hora con los minutos", introduce la hora en formato de 4 dígitos (ej. 1430 para las 14:30).

Enviar: Haz clic en el botón "Enviar".

Importante: Asegúrate de tener tu sesión de WhatsApp Web abierta en tu navegador predeterminado para que pywhatkit pueda enviar el mensaje.

2. Envío de Mensajes Múltiples/Instantáneos
Desde la ventana principal, haz clic en el botón "Envio multiple". Esto abrirá una nueva ventana.

Añadir Números:

Manualmente: En el campo "Ingresa aqui los numeros de telefono", introduce un número de 9 dígitos y haz clic en "Ingresar". El número se añadirá a la lista.

Desde CSV: Haz clic en el botón "Cargar archivo .csv". Selecciona un archivo CSV que contenga números de teléfono. La aplicación intentará extraer los números de la última columna, validando si son números españoles (6 o 7 al inicio) o si tienen el prefijo +34.

Eliminar Número: Selecciona un número de la lista y haz clic en "Eliminar" para quitarlo.

Mensaje: Escribe el mensaje que deseas enviar a todos los números de la lista en el área de texto "Mensaje".

Enviar: Haz clic en el botón "Enviar". Todos los mensajes se enviarán instantáneamente.

Importante: Al igual que con los mensajes programados, WhatsApp Web debe estar abierto.

Archivo de Icono
La aplicación utiliza un archivo de icono llamado WhatsApp.ico. Asegúrate de que este archivo se encuentre en el mismo directorio que el script app.py para que el icono se muestre correctamente en la ventana.

Manejo de Errores
La aplicación incluye un manejo básico de errores para entradas de teléfono y hora incorrectas, mostrando cuadros de mensaje informativos al usuario.