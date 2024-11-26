import shutil
import pygame # reproduce sonido
import tempfile #crear archivos temporales
from gtts import gTTS # convierte el texto en voz
from googletrans import Translator # toma el texto y lo traduce en el idioma indicado
from pathlib import Path  # Importamos pathlib para manejar rutas

class ControladorTextoAVoz: # clase controlador texto a voz
    
    def __init__(self): 
        
        pygame.mixer.init()  # Inicializar pygame para manejar el audio
        
        self.traductor = Translator()    # Inicializamos el traductor
        
        self.idiomas_validos = {   # listado de idiomas disponibles para traducir
            'Español': 'es',
            'Inglés': 'en',
            'Francés': 'fr',
            'Alemán': 'de',
            'Italiano': 'it',
            'Portugués': 'pt'
        }
        # Creamos instancia de la vista
        self.vista = None  # Lo inicializamos aquí, se asignará en el main

    def traducir_texto(self, texto, idioma_destino): # Este método toma un texto y un idioma de destino como entrada, y utiliza la biblioteca googletrans para traducir el texto al idioma indicado 
      
        try:
            # Realiza la traducción utilizando googletrans
            traduccion = self.traductor.translate(texto, dest=idioma_destino)
            return traduccion.text
        except Exception as e:
            print(f"Error al traducir el texto: {e}")
            return texto  # En caso de error, devolver el texto original

    def convertir_a_audio(self, texto, idioma, traducir=True): #  Convierte el texto a un archivo de audio MP3 usando gTTS.
      
        try:
            if traducir:
                # Traducir el texto antes de convertirlo a audio
                texto = self.traducir_texto(texto, idioma)
            
            tts = gTTS(text=texto, lang=idioma, slow=False)
            
            # Guardar en una carpeta temporal usando pathlib
            carpeta_temp = Path(tempfile.gettempdir())  # Carpeta temporal como objeto Path
            archivo_audio = carpeta_temp / "audio_generado.mp3"  # Construir ruta del archivo
            
            
            tts.save(str(archivo_audio))  # Guardar el archivo de audio en la ruta temporal
            
            # Mensaje de depuración
            print(f"Archivo temporal generado en: {archivo_audio}")
            
            return str(archivo_audio)  # Devolver como string para compatibilidad
        except Exception as e:
            print(f"Error al generar el archivo de audio: {e}")
            return None

    def reproducir_audio(self, archivo_audio): #reproduce un archivo de audio usando pygame.
       
        try:
            pygame.mixer.music.load(archivo_audio)
            pygame.mixer.music.play()

            # Esperar a que termine la reproducción
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            
            pygame.mixer.music.unload() # asegurarse de descargar el archivo después de la reproducción
        except Exception as e:
            print(f"Error al reproducir el archivo de audio: {e}")
    
    def guardar_audio(self, archivo_audio, ruta_destino): # guarda el archivo de audio en la ruta especificada.
      
        try:
            if archivo_audio:
                # Usar shutil para copiar el archivo a la ruta destino
                shutil.copy(archivo_audio, ruta_destino)
                print(f"Archivo guardado correctamente en: {ruta_destino}")
            else:
                print("No se encontró el archivo de audio para guardar.")
        except Exception as e:
            print(f"Error al guardar el archivo de audio: {e}")
