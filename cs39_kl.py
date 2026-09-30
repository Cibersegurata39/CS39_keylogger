#Es necesario descargarse las siguientes librerias
import tkinter as tk, logging
from datetime import datetime

print("")
print("   _____    _____           _____ ")
print("  / ____|  / ____|  ______ /  __ |")
print(" | |      | (___   |___  / \ \_| |")
print(" | |       \ __ \    |_  \  \__  |")
print(" | |____   ____) |  ___) |     | |")
print("  \_____| |_____/  |_____/     |_|")
print("")

#Archivo donde se guardará el registro
archivo= 'keylogger.txt'

#Configuramos logging una sola vez
logging.basicConfig(
  filename = archivo,
  level = logging.DEBUG,
  format = "%(asctime)s - %(message)s"
)

#Teclas pulsadas a ignorar
teclas_ign =["Shift_L",
    "Shift_R",
    "Control_L",
    "Control_R",
    "Alt_L",
    "Alt_R"
]

def marca_tiempo():
  timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  with open(archivo, "a", encoding="utf-8") as f:
    f.write(f"\n\n--- Inicio: {timestamp} ---\n")

def tecla(event):
  mensaje = f"Tecla pulsada: {event.keysym}"
  #Mostrar en la terminal
  print(mensaje)
  #Guardar en el archivo
  if event.keysym == "space":
    caracter = " "
  elif event.keysym == "Return":
    caracter = "\n"
  elif event.keysym in teclas_ign:
    return
  elif len(event.keysym) == 1:
    caracter = event.keysym
  else:
    caracter = f"[{event.keysym}]"
  #Reescribimos el contenido acumulado
  with open(archivo, "a", encoding="utf-8") as f:
    f.write(caracter)

#Se registra el momento en el que se escribe en el documento
marca_tiempo()

#Creación de la ventana donde probar el keylogger
ventana = tk.Tk()
ventana.title("Práctica de keylogger")
ventana.geometry("400x200")
#Creación de un mensaje en la ventana donde está el foco del keylogger
mensaje = tk.Label(
  ventana,
  text = "Prueba la herramienta cs39_kl!")
mensaje.pack(pady=70) #Centrar el texto a la ventana

#Detectar teclas mientras esta ventana tiene el foco
ventana.bind("<Key>", tecla)
ventana.mainloop()
