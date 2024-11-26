from gtts import gTTS # convertir texto a voz

class ModeloTextoAVoz: # clase modelo texto
    """Modelo que gestiona la conversión de texto a voz y la lista de idiomas disponibles."""

    def __init__(self): #inicializamos la clase
        
        self.idiomas_disponibles = { #  # listado de idiomas disponibles 
            'Español': 'es',
            'Inglés': 'en',
            'Francés': 'fr',
            'Alemán': 'de',
            'Italiano': 'it',
            'Portugués': 'pt',
            'Ruso': 'ru',
            'Chino': 'zh',
            'Japonés': 'ja',
            'Coreano': 'ko',
            'Árabe': 'ar',
        }

    def obtener_idiomas_disponibles(self): 

        return self.idiomas_disponibles # devuelve al listado de idiomas disponibles 

    def convertir_texto_a_voz(self, texto, idioma): # convierte el texto a un archivo de audio
        
        try:
            # Crear el objeto gTTS para convertir texto a voz
            tts = gTTS(text=texto, lang=idioma, slow=False)
            # Guardar el archivo de audio generado
            archivo_audio = "audio_generado.mp3"
            tts.save(archivo_audio)
            return archivo_audio
        except Exception as e:
            print(f"Error al generar el archivo de audio: {e}")
            return None
