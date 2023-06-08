from claseManejadorEmpleado import ManejadorEmpleado
if __name__=="__main__":
    dimension=int(input("Ingrese la dimension del arreglo"))
    empleados=ManejadorEmpleado(dimension)
    empleados.inicalizzarPlanta()
    empleados.inicializarContratados()
    empleados.inicializarExterno()
    #empleados.mostrar()
    #empleados.registrarHoras()
    #empleados.totalTareas()
    #empleados.ayudaEconomica()
    empleados.mostrarSueldo()




