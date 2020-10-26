class Persona:

    def __init__(self,nombre,apellido,dni,sexo):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.sexo=sexo

    def setNombre(self,nombre):
        self.nombre=nombre

    def setApellido(self,apellido):
        self.apellido=apellido

    def setDni(self,dni):
        self.dni=dni

    def setSexo(self,sexo):
        self.sexo=sexo

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getDni(self):
        return self.dni

    def getSexo(self):
        return self.sexo

