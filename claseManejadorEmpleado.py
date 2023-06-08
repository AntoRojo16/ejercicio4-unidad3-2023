import numpy as np
from claseEmpleado import Empleado
from claseContratado import Contratado
from clasePlanta import Planta
from claseExterno import Externo
import csv
class ManejadorEmpleado:
    __cantidad=0



    def __init__(self,dimension):
        self.__empleados=np.empty(dimension,dtype=Empleado)
        self.__cantidad=0

    def agregarEmpleado(self,unEmpleado):
        self.__empleados[self.__cantidad]=(unEmpleado)
        self.__cantidad=self.__cantidad+1



    def inicalizzarPlanta(self):
        archivo=open("plata.csv")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
                dni=fila[0]
                nombre=fila[1]
                direccion=fila[2]
                telefono=fila[3]
                sueldo=fila[4]
                antiguedad=fila[5]
                unEmpleado=Planta(dni,nombre,direccion,telefono,sueldo,antiguedad)
                self.agregarEmpleado(unEmpleado)
        archivo.close()


    def inicializarContratados(self):
        archivo=open("contratados.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:

            dni=fila[0]
            nombre=fila[1]
            direccion=fila[2]
            telefono=fila[3]
            fechaIn=fila[4]
            fechaFin=fila[5]
            cantH=fila[6]
            valor=fila[7]
            unEmpledo=Contratado(dni,nombre,direccion,telefono,fechaIn,fechaFin,cantH,valor)
            self.agregarEmpleado(unEmpledo)
        archivo.close()

    def inicializarExterno(self):
        archivo=open("externo.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:

            dni=fila[0]
            nombre=fila[1]
            direccion=fila[2]
            telefono=fila[3]
            tarea=fila[4]
            fechaIn=fila[5]
            fechaFin=fila[6]
            monto=fila[7]
            costo=fila[8]
            montoS=fila[9]
            unEmpledo=Externo(dni,nombre,direccion,telefono,tarea,fechaIn,fechaFin,monto,costo,montoS)
            self.agregarEmpleado(unEmpledo)



    def mostrar(self):

        for i in range(self.__cantidad):
            self.__empleados[i].mostrarDatos()


    def registrarHoras(self):
        dni=input("ingrese el dni")
        horas=input("ingresar cantidad de horas tranbajadas el dia de hoy")
        bandera=False
        i=0
        while(i<self.__cantidad)and(bandera==False):
            if isinstance(self.__empleados[i],Contratado):
                if int(self.__empleados[i].getDni())==int(dni):
                    self.__empleados[i].mostrarDatos()
                    self.__empleados[i].modificarCantidadeHoras(horas)
                    bandera=True
            i=i+1


    def totalTareas(self):
        tarea=input("ingrese el nombre de una tarea")
        fecha=input("ingrese la fecha actual")
        bandera=False
        i=0
        while(i<self.__cantidad)and(bandera==False):
            if isinstance(self.__empleados[i],Externo):
                if self.__empleados[i].getTarea()==tarea:
                    bandera=self.__empleados[i].verificarFecha(fecha)
                    if bandera==True:
                        self.__empleados[i].mostrarTotal()
            i=i+1


    def ayudaEconomica(self):
        for i in range(self.__cantidad):
            if isinstance(self.__empleados[i],Planta):
                print(self.__empleados[i].getSueldo())
                if self.__empleados[i].getSueldo()<150000:
                    print("Necesita la ayuda economica")
                    print(self.__empleados[i].mostrarDAtosSueldo())



    def mostrarSueldo(self):
        for i in range(self.__cantidad):
            print(self.__empleados[i].calcularSueldo())
            self.__empleados[i].mostrarSueldo()


