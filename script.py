import Time
import Faker
import ListaDoble
import abb
import avl
import arbol23
import hashh

def elegir (self,eleccion):
    tipo = input ("Elija un numero según el tipo de estructur")
    print("1. Lista doble\n 2.abb \n 3.AVL \n 4.2-3Tree \n 5.Hash \n")
    if tipo == 1:
        eleccion = input("que desea hacer?")
        print("1.agregar contacto \n 2.Eliminar contacto \n 3.Imprimir agenda")
        if eleccion == 1:
          nombre = input ("ingrese los datos del contacto separados por un espacio")
          ListaDoble.insert(nombre)
        elif eleccion == 2:
            lastname == input ("ingrese apellido del contacto a eliminar")    
            ListaDoble.eliminashon (lastname)
        elif eleccion == 3:
            ListaDoble.imprimir()
    if tipo == 2:
         eleccion = input("que desea hacer?")
        print("1.agregar contacto \n 2.Eliminar contacto \n 3.Imprimir agenda")
        if eleccion == 1:
          nombre = input ("ingrese los datos del contacto separados por un espacio")
          abb.insert(nombre)
        elif eleccion == 2:
            lastname == input ("ingrese apellido del contacto a eliminar")    
            abb.delete(lastname)
        elif eleccion == 3:
            abb.imprimir_in_order()

    if tipo == 3:
         eleccion = input("que desea hacer?")
        print("1.agregar contacto \n 2.Eliminar contacto \n 3.Imprimir agenda")
        if eleccion == 1:
          nombre = input ("ingrese los datos del contacto separados por un espacio")
          avl.insertar(nombre)
        elif eleccion == 2:
            lastname == input ("ingrese apellido del contacto a eliminar")    
            avl.eliminar(lastname)
        elif eleccion == 3:
            avl.imprimir_in_order()
    

    if tipo == 5:
        eleccion = input("que desea hacer?")
        print("1.agregar contacto \n 2.Eliminar contacto \n 3.Imprimir agenda")
        if eleccion == 1:
          nombre = input ("ingrese los datos del contacto separados por un espacio")
          hashh.insert(nombre)
        elif eleccion == 2:
            lastname == input ("ingrese apellido del contacto a eliminar")    
            hashh.eliminar(lastname)
        elif eleccion == 3:
            hashh.imprimir_in_order()


