class Banda():

    """
    Clase que representa una banda musical.

    Atributos:
        nombre (str): El nombre de la banda.
        genero (str): El genero de la banda.
        _integrantes (list): Lista de integrantes de la banda.

    Atributos de clase:
        generos (set): Conjunto de generos de todas las bandas creadas.

    Métodos:
        __init__(nombre, genero="None"): Constructor de la clase Banda.
        integrantes: Propiedad de solo lectura para acceder a la lista de integrantes.
        integrantes(lista): Setter para asignar la lista de integrantes.
        __str__(): Representacion en forma de cadena de la banda.

    """
    
    generos = set()
        
    def __init__(self, nombre, genero="None"):
        self.nombre=nombre
        self.genero=genero
        self._integrantes=[]
        Banda.generos.add(genero)
        
    @property    
    def integrantes(self):
         return self._integrantes
    
    @integrantes.setter
    def integrantes(self, lista):
         self._integrantes = lista
    
    def __str__(self):
        texto = f"La banda de {self.genero} {self.nombre} está integrada por: "
        for elem in self._integrantes:
            texto += f"\n{elem}"
        return texto
    