# Convertidortextoavoz
Mi primer proyecto 
Aplicacion: CONVERSION DE TEXTO A VOZ

Objetivo:
El objetivo principal de la aplicación es convertir texto a voz en varios idiomas. Los usuarios
podrán cargar un archivo .txt o introducir manualmente el texto, con la opción de guardar y
reproducir los archivos de audio generados.

Descripción:
La aplicación que he desarrollado permite al usuario introducir manualmente el texto que desea
convertir o cargar un archivo .txt, cuyo contenido se mostrará en un cuadro de texto editable. A
continuación, podrá seleccionar el idioma deseado para la traducción mediante un menú
desplegable. Una vez traducido el texto, la aplicación permitirá convertirlo a voz y, finalmente,
exportar el audio generado.

Funcionalidades:
● La Vista está desarrollada con la librería CustomTkinter, una versión personalizada de
Tkinter que permite diseñar interfaces más modernas. La interfaz gráfica proporciona una
experiencia de usuario amigable y simplificada para realizar las tareas de conversión de
texto a voz. Posee una entrada de texto, selección de idiomas y botones de acción (
Convertir a voz, Exportar audio y cargar archivo txt)
● El Controlador es la capa intermedia que conecta la Vista con el Modelo, manejando la
lógica de la aplicación y gestionando la interacción del usuario. Contiene métodos que se
encargan de realizar la conversión del texto a audio, traducción del texto (si es necesario)
y reproducción del audio.
● El Modelo maneja la conversión de texto a audio y la gestión de idiomas disponibles. A
pesar de no tener acceso directo a la interfaz de usuario, el Modelo proporciona toda la
lógica relacionada con la conversión de texto a voz.
