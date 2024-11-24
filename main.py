from controlador import ControladorTextoAVoz #  Importamos la clase ControladorTextoAVoz desde un módulo llamado controlador
from vista import VistaTextoAVoz #Importa la clase VistaTextoAVoz desde un módulo llamado vista

if __name__ == "__main__":
    controlador = ControladorTextoAVoz()  # Creamos la instancia del controlador
    vista = VistaTextoAVoz(controlador)  # Pasamos el controlador a la vista
    vista.mainloop()  # Iniciamos el bucle principal de la aplicacion