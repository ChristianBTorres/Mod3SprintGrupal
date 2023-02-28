from bodega import Bodega 
from clientes import Clientes
from ventas import Pedidos
clientes = Clientes()
bodega=Bodega()
pedido=Pedidos()
#Importar y crear instancias para las clases


while True:
 opcion = input("\nHola, cómo estás?\nSelecciona una de las siguientes opciones:\n1.- BODEGA \n2.- CLIENTES \n3.- VENTAS\n4.- SALIR\n>")
 if opcion == '1':
    bodega.menu()
 elif opcion == '2':
    clientes.menu()
 elif opcion == '3':
    pedido.menu()
 elif opcion == '4':
    print("EXIT")
    break
 else:
  print("Seleccione una opción válida...")









