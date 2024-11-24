from gtts import gTTS

class ModeloTextoAVoz:
    """Modelo que gestiona la conversión de texto a voz y la lista de idiomas disponibles."""

    def __init__(self):
        # Diccionario de idiomas disponibles (código del idioma: nombre del idioma)
        self.idiomas_disponibles = {
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
        """Devuelve el diccionario de idiomas disponibles."""
        return self.idiomas_disponibles

    def convertir_texto_a_voz(self, texto, idioma):
        """
        Convierte el texto a un archivo de audio MP3 usando gTTS.
        
        :param texto: Texto a convertir.
        :param idioma: Código del idioma (por ejemplo, 'es' para español).
        :return: Ruta del archivo MP3 generado.
        """
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