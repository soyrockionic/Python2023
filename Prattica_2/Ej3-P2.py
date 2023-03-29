jupyter_info = """JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones."""

frase = jupyter_info.split(' ')

letra = input("Ingresa una letra ")
if(letra).isalpha() :
    for i in frase :
        if i[0] == letra :
            print(i)
else :
    print('No has ingresado ninguna letra') 