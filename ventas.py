from bodega import Bodega
import random
bodega = Bodega()
class Pedidos():
    def __init__(self): # Inicializar variables
      self.bodega_a = {}
      self.bodega_b = {}
      self.cant_a = 0
      self.cant_b = 0


    def enviar_producto(self): #Proceso de distribucion entre las bodegas
        while True:
            distancia = int(input('Ingrese distancia en Kilometros: '))
            bodega.listar() #Mostrar la lista de productos para recordar los ids
            producto = int(input("Ingrse el ID del producto que desea agregar: "))
            try: #Validar existencia del producto
                print(bodega.stock[producto]['nombre'], "- Stock disponible:",bodega.stock[producto]['stock'])
            except:
                print("Producto no existe")
                continue
            stock = int(input('Ingresar Stock: '))

            

            if (distancia < 1000) and (stock <= bodega.stock[producto]['stock']): #Validar disponibilidad de stock y clacificar por ditancia
                
                if (self.cant_a+stock) <= 500: #Validar espacio en bodega
                    self.bodega_a[random.randint(10000,99999)]= {'id_producto':bodega.stock[producto],'producto':bodega.stock[producto]['nombre'],'cantidad':stock}
                    self.cant_a+=stock
                    break
                else:
                    print("La cantidad solicitada exede la capacidad de la bodega (500)\nCantidad actual:",self.cant_a,"\nCantidad solicitada:",stock)
            elif (distancia >= 1000) and (stock <= bodega.stock[producto]['stock']): #Validar disponibilidad de stock y clacificar por ditancia
                
                if (self.cant_b+stock) <= 500: #Validar espacio en bodega
                    self.bodega_b[random.randint(10000,99999)]= {'id_producto':bodega.stock[producto],'producto':bodega.stock[producto]['nombre'],'cantidad':stock}
                    self.cant_b+=stock
                    break
                else:
                    print("La cantidad solicitada exede la capacidad de la bodega (500)\nCantidad actual:",self.cant_b,"\nCantidad solicitada:",stock)
            else:
                print('Stock insuficiente')


    def pedidos(self): #Listar pedidos por bodega
        print("Pedidos (Envío rápido)")
        for x in self.bodega_a:
            print("ID Pedido:",x,"Producto:",x['nombre'],"Cantidad:",x['cantidad'])

        print("Pedidos (Envío lento)")
        for x in self.bodega_b:
            print(x)

    def menu(self):
        while True:
            opcion = input("1.-Realizar pedido \n2.-Ver pedidos\n3.- Salir\n>")
            if opcion == '1':
                self.enviar_producto()
            elif opcion == '2':
                self.pedidos()
            elif opcion == '3':
                print("EXIT")
                break
            else:
                print("Seleccione una opción válida...")