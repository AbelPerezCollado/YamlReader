import yaml

class YamlReader():
    def __init__(self):
        self.data = None
        
    def load_file(self,path):
        """
        Carga el archivo YAML desde la ruta especificada.

        Args:
            path (str): La ruta al archivo YAML.

        Returns:
            dict: Los datos cargados desde el archivo YAML 
                  en forma de diccionario, o None si hay 
                  algún error.
        """
        try:
            with open(path, 'r') as file:
                self.data = yaml.safe_load(file)
            return self.data
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{path}'")
            return None
        except yaml.YAMLError as error:
            print(f"Error al cargar el archivo yaml '{path}': {error} ")
            return None
        
    def save_file(self, path):
        """
        Guarda los datos actuales en un archivo YAML en la ruta especificada.

        Args:
            path (str): La ruta al archivo YAML.

        Returns:
            bool: True si los datos se guardaron correctamente, False si hay algún error.
        """
        if self.data is None:
            print("Error: No hay datos para guardar.")
            return False

        try:
            with open(path, 'r+') as file:
                yaml.safe_dump(self.data, file)
            return True
        except yaml.YAMLError as e:
            print(f"Error al guardar el archivo YAML '{path}': {e}")
            return False