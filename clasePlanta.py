from claseEmpleado import Empleado
class Planta(Empleado):
    __sueldo=0
    __antiguedad=0



    def __init__(self,dni,nombre,direccion,telefono,sueldo,antiguedad):
        super().___init__(dni,nombre, direccion, telefono)
        self.__sueldo=int(sueldo)
        self.__antiguedad=antiguedad


    def calcularSueldo (self):
        sueldo=self.__sueldo+1%self.__sueldo*int(self.__antiguedad)
        return sueldo


    def getSueldo(self):
        return self.__sueldo



    def mostrarDAtosSueldo(self):
        super().mostrar()

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Sueldo {}, Antigüedad {}".format(self.__sueldo,self.__antiguedad))

            
