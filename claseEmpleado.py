class Empleado:
    __DNI=0
    __nombre=""
    __direccion=""
    __telefono=0




    def ___init__ (self,dni,nombre,direccion,telefono):
        self.__DNI=dni
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono


    def calcularSueldo(self):
        pass


    def mostrar(self):
        print("Nobre {}, Direccion {}, DNI {}".format(self.__nombre,self.__direccion,self.__DNI))



    def getDni(self):
        return self.__DNI


    def mostrarSueldo(self):
        print(" su nombre es {}, sue telefono es {}".format(self.__nombre,self.__telefono))

    def mostrarDatos(self):
        print("los datos del empleado son \nDNI {},nombre {},direccion {},telefono {}".format(self.__DNI,self.__nombre,self.__direccion,self.__telefono))




