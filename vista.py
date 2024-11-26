import customtkinter as ctk # libreria para crear la interfaz
from tkinter import filedialog, messagebox 

class VistaTextoAVoz(ctk.CTk): # esta clase hereda de ctk.CTk y se encarga de crear y gestionar la interfaz gráfica.
    
    def __init__(self, controlador): #inicializa la ventana principal
        super().__init__()
        self.title("Texto a Voz")
        self.geometry("600x600")  # Aumentar tamaño de la ventana para más opciones
        self.controlador = controlador
        self.controlador.vista = self  # Pasar la vista al controlador

        self.crear_widgets()

    def crear_widgets(self): # Crea todos los elementos de la interfaz, como etiquetas, botones, cuadros de texto y un menú desplegable para seleccionar el idioma.

        
        self.lbl_texto = ctk.CTkLabel(self, text="Introduce el texto o carga un archivo:", text_color="black")
        self.lbl_texto.pack(pady=10)

        # Botón para cargar un archivo de texto
        self.btn_cargar_archivo = ctk.CTkButton(self, text="Cargar archivo .txt", command=self.cargar_archivo_txt)
        self.btn_cargar_archivo.pack(pady=10)

        # Cuadro de texto donde se mostrará el contenido del archivo o texto manual
        self.txt_texto = ctk.CTkTextbox(self, height=200, width=450, fg_color="lightgrey", text_color="black")
        self.txt_texto.pack(pady=10)

        self.lbl_idioma = ctk.CTkLabel(self, text="Seleccione el idioma:", text_color="black")
        self.lbl_idioma.pack(pady=10)

        self.combo_idioma = ctk.CTkComboBox(self, values=list(self.controlador.idiomas_validos.keys()))
        self.combo_idioma.pack(pady=10)

        # Botón para convertir texto a voz
        self.btn_convertir = ctk.CTkButton(self, text="Convertir a voz", command=self.convertir_texto_a_voz)
        self.btn_convertir.pack(pady=20)

        # Botón para exportar el audio generado
        self.btn_exportar = ctk.CTkButton(self, text="Exportar Audio", command=self.exportar_audio)
        self.btn_exportar.pack(pady=10)

    def cargar_archivo_txt(self): # Abre un diálogo para seleccionar un archivo de texto y carga su contenido 
        """Carga el contenido de un archivo de texto en el cuadro de texto."""
        archivo_ruta = filedialog.askopenfilename(
            title="Seleccionar archivo",
            filetypes=[("Archivos de texto", "*.txt")]
        )

        if archivo_ruta:
            try:
                with open(archivo_ruta, 'r', encoding='utf-8') as archivo:
                    contenido = archivo.read()
                    # Mostrar el contenido en el cuadro de texto
                    self.txt_texto.delete("1.0", "end")  # Borrar contenido previo
                    self.txt_texto.insert("1.0", contenido)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo.\n{e}")

    def convertir_texto_a_voz(self):
        """Convierte el texto ingresado a voz al idioma seleccionado."""
        texto = self.txt_texto.get("1.0", "end-1c")  # Obtener el texto del cuadro de texto
        idioma = self.combo_idioma.get()  # Obtener el idioma seleccionado

        # Verificar si el texto no está vacío
        if texto.strip() == "":
            messagebox.showerror("Error", "No se ingresó texto.")
            return

        # Verificar si el idioma es válido
        if idioma not in self.controlador.idiomas_validos:
            messagebox.showerror("Error", f"Idioma '{idioma}' no válido.")
            return
            
        archivo_audio = self.controlador.convertir_a_audio(texto, self.controlador.idiomas_validos[idioma]) # convertir texto a voz
      
        if archivo_audio:
            self.controlador.reproducir_audio(archivo_audio)
            messagebox.showinfo("Éxito", "Texto convertido a voz correctamente.")
        else:
            messagebox.showerror("Error", "Hubo un problema al generar el audio.")
    
    def exportar_audio(self):
        """Permite al usuario exportar el audio generado a una ubicación de su elección."""
        texto = self.txt_texto.get("1.0", "end-1c")
        idioma = self.combo_idioma.get()
       
        if texto.strip() == "":
            messagebox.showerror("Error", "No se ingresó texto.") # Verificar si hay texto ingresado
            return
        
        if idioma not in self.controlador.idiomas_validos: # Verificar si el idioma es válido
            
            messagebox.showerror("Error", f"Idioma '{idioma}' no válido.")
            return
        
        archivo_audio = self.controlador.convertir_a_audio(texto, self.controlador.idiomas_validos[idioma])  #Convertir el texto a voz

        if archivo_audio:
            # Abrir el cuadro de diálogo para elegir la ubicación de exportación
            ruta_destino = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Archivos MP3", "*.mp3")])
            if ruta_destino:
                # Guardar el archivo en la ruta seleccionada
                self.controlador.guardar_audio(archivo_audio, ruta_destino)
                messagebox.showinfo("Éxito", f"Audio exportado correctamente a {ruta_destino}")
            else:
                messagebox.showwarning("Advertencia", "No se seleccionó una ubicación para guardar el archivo.")
        else:
            messagebox.showerror("Error", "Hubo un problema al generar el audio para exportar.")
