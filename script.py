import ListaDoble
import abb
import avl
import hashh

def __main__ ():
    tipo = input ("Elija un numero segun el tipo de estructur")
    print("1. Lista doble\n 2.abb \n 3.AVL \n 4.2-3Tree \n 5.Hash \n")
    if tipo == 1:
        eleccion = input("que desea hacer?")
        print("1.Agregar contact \n 2.Eliminar contacto \n 3.Imprimir agenda \n")
        l= ListaDoble()
        if eleccion == 1:
          nombre = input ("ingrese los datos del contacto separados por un espacio")
          l.insert(nombre)
        elif eleccion == 2:
            lastname == input ("ingrese apellido del contacto a eliminar")    
            l.eliminashon (lastname)
        elif eleccion == 3:
            l.imprimir()
    if tipo == 2:
        eleccion = input("que desea hacer?")
        print("1.agregar contacto \n 2.Eliminar contacto \n 3.Imprimir agenda \n")
        ab = abb()
        if eleccion == 1:
          nombre = input ("ingrese los datos del contacto separados por un espacio")
          ab.insert(nombre)
        elif eleccion == 2:
            lastname == input ("ingrese apellido del contacto a eliminar")    
            ab.delete(lastname)
        elif eleccion == 3:
            ab.imprimir_in_order()

    if tipo == 3:
        eleccion = input("que desea hacer?")
        print("1.agregar contacto \n 2.Eliminar contacto \n 3.Imprimir agenda \n")
        av = avl()
        if eleccion == 1:
          nombre = input ("ingrese los datos del contacto separados por un espacio")
          av.insertar(nombre)
        elif eleccion == 2:
            lastname == input ("ingrese apellido del contacto a eliminar")    
            av.eliminar(lastname)
        elif eleccion == 3:
            av.imprimir_in_order()
    if tipo == 4:
        print ("Opcion en mantenimiento, por favor elige otra opcion")
        elegir()

    if tipo == 5:
        eleccion = input("que desea hacer?")
        print("1.agregar contacto \n 2.Eliminar contacto \n 3.Imprimir agenda \n")
        o = hashh()
        if eleccion == 1:
          nombre = input ("ingrese los datos del contacto separados por un espacio")
          o.insert(nombre)
        elif eleccion == 2:
            lastname == input ("ingrese apellido del contacto a eliminar")    
            o.eliminar(lastname)
        elif eleccion == 3:
            o.imprimir_in_order()


