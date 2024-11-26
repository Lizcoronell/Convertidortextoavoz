mport shutil
import pygame  # Reproduce sonido
import tempfile  # Crear archivos temporales
from gtts import gTTS  # Convierte el texto en voz
from googletrans import Translator  # Toma el texto y lo traduce en el idioma indicado
from pathlib import Path  # Importamos pathlib para manejar rutas

class ControladorTextoAVoz:  # Clase controlador texto a voz

    def __init__(self): 
        pygame.mixer.init()  # Inicializar pygame para manejar el audio
        self.traductor = Translator()  # Inicializamos el traductor
        
        self.idiomas_validos = {  # Listado de idiomas disponibles para traducir
            'Español': 'es',
            'Inglés': 'en',
            'Francés': 'fr',
            'Alemán': 'de',
            'Italiano': 'it',
            'Portugués': 'pt'
        }
        # Creamos instancia de la vista
        self.vista = None  # Lo inicializamos aquí, se asignará en el main

    def traducir_texto(self, texto, idioma_destino): 
        try:
            # Realiza la traducción utilizando googletrans
            traduccion = self.traductor.translate(texto, dest=idioma_destino)
            
            if traduccion and hasattr(traduccion, 'text'):  # Verificamos que la traducción sea válida
                return traduccion.text
            else:
                print("Error en la traducción: No se obtuvo un texto válido.")
                return texto  # En caso de error, devolver el texto original
        except Exception as e:
            print(f"Error al traducir el texto: {e}")
            return texto  # En caso de error, devolver el texto original

    def convertir_a_audio(self, texto, idioma, traducir=True): 
        try:
            if traducir:
                # Traducir el texto antes de convertirlo a audio
                texto = self.traducir_texto(texto, idioma)
            
            # Comprobar si el texto traducido es válido
            if not texto:
                print("El texto está vacío después de la traducción.")
                return None
            
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

    def reproducir_audio(self, archivo_audio): 
        try:
            if archivo_audio is None:
                print("No se puede reproducir el archivo: archivo_audio es None.")
                return
            
            pygame.mixer.music.load(archivo_audio)
            pygame.mixer.music.play()

            # Esperar a que termine la reproducción
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            pygame.mixer.music.unload()  # Asegurarse de descargar el archivo después de la reproducción
        except Exception as e:
            print(f"Error al reproducir el archivo de audio: {e}")

    def guardar_audio(self, archivo_audio, ruta_destino): 
        try:
            if archivo_audio:
                # Usar shutil para copiar el archivo a la ruta destino
                shutil.copy(archivo_audio, ruta_destino)
                print(f"Archivo guardado correctamente en: {ruta_destino}")
            else:
                print("No se encontró el archivo de audio para guardar.")
        except Exception as e:
            print(f"Error al guardar el archivo de audio: {e}")
