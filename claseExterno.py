from claseEmpleado import Empleado
class Externo(Empleado):
    __terea=""
    __fechaIn=0
    __fechaFin=0
    __montoViatico=0
    __costo=0
    __montoS=0


    def __init__ (self,dni,nombre,direccion,telefono,tarea,Fein,fin,montoT,costo,montoS):
        super().___init__(dni,nombre,direccion,telefono)
        self.__terea=tarea
        self.__fechaIn=Fein
        self.__fechaFin=fin
        self.__montoViatico=montoT
        self.__costo=costo
        self.__montoS=montoS

    def calcularSueldo (self):
        sueldo=int(self.__costo)-int(self.__montoViatico)-int(self.__montoS)
        return sueldo

    def mostrarDatos(self):
        super().mostrarDatos()
        print("terea {}, fecha de incio {}, fecha de finalizacion {}, monto de viatico {}, costo de la obra {}, monto del seguro de vida {}".format(self.__terea,self.__fechaIn,self.__fechaFin,self.__montoViatico,self.__costo,self.__montoS))


    def getTarea(self):
        return self.__terea



    def verificarFecha(self,fecha):
        bandera=False
        if fecha<self.__fechaFin:
            bandera=True
        else:
            bandera=False
        return bandera


    def mostrarTotal(self):
        print("El total de esta tarea es {}".format(self.__montoViatico))
