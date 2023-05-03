class Recurso:

    def __init__(self, nombre, url, tipo, ultima_modificacion):
        self.__nombre = nombre
        self.__url = url
        self.__tipo = tipo
        self.__ultima_modificacion = ultima_modificacion

    def dar_nombre(self,nombre):
        self.__nombre = nombre

    def agregar_url(self,url):
        self.__url = url

    def agregar_tipo(self,tipo):
        self.__tipo = tipo

    def agregar_fecha(self,fecha):
        self.__ultima_modificacion = fecha

    def get__nombre(self):
        return self.__nombre

    def get__url(self):
        return self.__url

    def get__tipo(self):
        return self.__tipo

    def get__ultima_modificacion(self):
        return self.__ultima_modificacion

    def __str__(self):
        return f"{self.__nombre} ({self.__tipo}) - última modificación: {self.__ultima_modificacion}"

# Creamos algunos recursos para el curso de Python
recurso1 = Recurso("Introducción a Python", "https://example.com/intro-python", "video", "2023-05-05")
recurso2 = Recurso("Ejercicios de Python básico", "https://example.com/ejercicios-python", "jupyter", "2023-05-04")
recurso3 = Recurso("Guía de estilo de Python", "https://example.com/guia-estilo-python.pdf", "PDF", "2023-05-04")

print('*'*70)
recurso1.dar_nombre('Introducion a PYSimpleGUI')
print(recurso1)
print('*'*70)
print(recurso2)
print('*'*70)
print(recurso3)
print('*'*70)