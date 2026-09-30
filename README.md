# CS39_keylogger

<img src="https://img.shields.io/badge/-python-3776AB?style=for-the-badge&logo=python&logoColor=white" />


> [!NOTE]
> La herramienta **CS39_keylogger** ha sido creada con fines educativos, por eso su rango de acción se limita a una ventana diseñada específicamente.

El programa es un *keylogger* creado con Python que almacena las teclas pulsadas en un archivo *txt*.
El funcionamiento del mismo es el siguiente:

Al iniciar el programa por terminal, desde la carpeta que lo contiene, ocurren dos cosas. Por un lado, por medio de la función <code>marca_tiempo()</code>, se crea el archivo donde se almacenarán las teclas pulsadas y a su vez, se registrará en él la marca temporal en la que se empieza a escribir. Este archivo se crea en modo *append* para que no sobrescriba lo ya guardado anteriormente y en la misma carpeta desde donde se inició el programa.
Por otro lado se crea y abre una pequeña ventana, cuya función es tener el foco del programa e ir guardando las teclas que se pulsan con la ventana abierta. De esta manera, se evita que el *keylogger* actúe en otras ventanas y se puede conseguir una prueba acotada, segura y no malintencionada. Todo esto se hace con los métodos *title*, *geometry* y *Label* de la clase Tk.

Con el método *bind* se controla que, al ocurrir un evento de teclado en la ventana creada, se llame a la función <code>tecla</code>. Esta función imprime por la pantalla del terminal la tecla pulsada y además, la guarda en el documento de texto sin sobrescribir lo almacenado anteriormente. Al tocar teclas distintas a letras o números se muestra el nombre de la tecla pulsada. Es decir, no recoge el valor de los caracteres especiales. Por ejemplo, puedes teclear el signo de exclamación y aparecerá el valor *exclamation*. Pues bien, mediante un <code>if/else</code>, se cambia el valor de algunos de estos caracteres como *space* por un espacio y el de *Return* por un salto de línea. Por su parte, las letras y números se guardan como tales, el resto de caracteres sí que mostrarán su nombre y no el carácter que le correspondería. Además se ignorarán una serie de teclas como *shift*, *Alt* y *Alt Gr* para que sea más intuitivo el texto guardado en el documento.

Por último, para mantener el *keylogger* funcionando dentro de la ventana, se utiliza el método *mainloop*. Mientras no se cierre la ventana se escribirán todas las teclas que se vayan pulsando.


<img width="732" height="513" alt="Captura de pantalla 2026-09-30 180106" src="https://github.com/user-attachments/assets/76cd50a7-7aed-4e95-b037-c4c65c71634a" />

Ventana creada y terminal donde se muestran las teclas que se van pulsando.

<img width="1397" height="252" alt="Captura de pantalla 2026-09-30 180212" src="https://github.com/user-attachments/assets/ebe86eba-5a4b-48bd-b27c-a145f7f51935" />

Documento de texto donde se guardan las teclas pulsadas.
