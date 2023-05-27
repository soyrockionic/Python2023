import datetime

class Recurso:

    """
    Clase que representa un recurso del curso.

    Atributos:
        nombre (str): El nombre del recurso.
        url (str): La URL donde se puede encontrar el recurso.
        tipo (str): El tipo de recurso (ej. video, jupyter, PDF).
        ultima_modificacion (str): La fecha de la ultima modificacion del recurso (formato AAAA-MM-DD).
    """

    def __init__(self, nombre, url, tipo):
        self._nombre = nombre
        self._url = url
        self._tipo = tipo
        self._ultima_modificacion = datetime.date.today()

    def set_nombre(self,nombre):
        self._nombre = nombre

    def set_url(self,url):
        self._url = url

    def set_tipo(self,tipo):
        self._tipo = tipo

    def set_fecha(self,fecha):
        self._ultima_modificacion = fecha

    def get_nombre(self):
        return self._nombre

    def get_url(self):
        return self._url

    def get_tipo(self):
        return self._tipo

    def get_ultima_modificacion(self):
        return self._ultima_modificacion

    def __str__(self):
        return f"{self._nombre} - {self._url} ({self._tipo}) - ultima modificacion: {self._ultima_modificacion}"
