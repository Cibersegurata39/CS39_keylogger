# CS39_keylogger

<img src="https://img.shields.io/badge/-python-3776AB?style=for-the-badge&logo=python&logoColor=white" />

La herramienta **CS39_keylogger** ha sido creada con fines educativos, por eso su rango de acción se limita a una ventana diseñada especificamente. El programa es un *keylogger* creado con Python que almacena las teclas pulsadas en un archivo *txt*.

El funcionamiento del programa es el siguiente. Al arrancarlo por terminal, desde la carpeta que lo contiene, ocurren dos cosas. Por un lado, por medio de la función <code>marca_tiempo()</code>, se crea el archivo donde se almacenarán las teclas pulsadas y a su vez, se registrará en él la marca temporal en la que se empieza a escribir. Este archivo se crea en modo *append* para que no sobrescriba lo ya guardado anteriormente.
Por otro lado se crea y abre una pequeña ventana, cuya función es tener el foco del programa e ir guardando las teclas que se pulsan con la ventana abierta. De esta manera, se evita que el *keylogger* actúe en otras ventanas y se puede conseguir una prueba acotada, segura y no malintencionada. Todo esto se hace con los métodos *title*, *geometry* y *Label* de la clase Tk.

Con el método *bind* se controla que al ocurrir un evento de teclado en la ventana creada se llame a la función <code>tecla</code>.


Para mantener la ventana funcionando se utiliza el método *mainloop*, el *keylogger* seguirá ejecutandose hasta cerrarla.







