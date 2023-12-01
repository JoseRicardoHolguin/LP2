print("Proyecto final Jose Holguin")

class Empleados:
    def __init__(self, nombre, apellido_paterno, edad, sexo):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.edad = edad
        self.sexo = sexo

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido Paterno: {self.apellido_paterno}, Edad: {self.edad}, Sexo: {self.sexo}'