import time
import random
class Bodega():
    def __init__(self): #Crear stock de productos en bodega
        self.stock = {random.randint(10000,99999):{'nombre':'vasos', 'stock':random.randint(300,500)}, 
                      random.randint(10000,99999):{'nombre':'cuchara', 'stock':random.randint(300,500)}, 
                      random.randint(10000,99999):{'nombre':'cuchillo', 'stock':random.randint(300,500)}, 
                      random.randint(10000,99999):{'nombre':'tenedor', 'stock':random.randint(300,400)}}

    def menu(self): 
        while True:
            opcion = input("1.- Agregar Productos \n2.- Eliminar Productos \n3.- Verificar Stock\n4.- Listar Productos\n5.- Actualizar Stock\n6.- Salir\n>")
            if opcion == '1':
                self.agregar()
            elif opcion == '2':
                self.eliminar()
            elif opcion == '3':
               self.verificarstock()
            elif opcion == '4':
                self.listar()  
            elif opcion == '5':
                self.actualizar() 
            elif opcion == '6':
                print("EXIT")
                break
            else:
                print("Seleccione una opción válida...")


    def agregar(self):
        while True:
            id = random.randint(10000,99999) #Crear id aleatorio
            if id not in self.stock: #Validar que el id no exista en el diccionario
                nombre = input("Ingrese Nombre de nuevo producto\n")
                stock = (int(input("Ingrese Stock: \n")))
                self.stock[id]={'nombre':nombre, 'stock':stock}
                break


        

    def listar(self):
        for keys in self.stock:
            print("ID:" ,keys,"\nNombre:" ,self.stock[keys]['nombre'],"\nStock:" ,self.stock[keys]['stock'],"\n")
            time.sleep(1)

    def eliminar(self):
        while True:
            key = input("Ingrese ID del producto que desea eliminar: ")
            try:
                key = int(key)
                del self.stock[key]
                break
            except:
                print("Ingrese un producto existente")


    def verificarstock(self):
        for keys in self.stock:
            if self.stock[keys]['stock']<400:
                print(f"El producto '{self.stock[keys]['nombre']}' posee menos de 400 unidades (Unidades disponibles:{self.stock[keys]['stock']})")




    def actualizar(self): #Modificar productos
        while True:
            key = input("Ingrese el ID del producto que desea modificar: ")
            key = int(key)
            try: 
                print(f"Nombre: {self.stock[key]['nombre']}\nStock: {self.stock[key]['stock']}")

                while True:
                    opcion = input("Ingrese la opción: \n1.Sumar\n2.Restar\n3.Salir")
                    if opcion == '1':
                        sumar=int(input('Ingrese cantidad a sumas: '))
                        self.stock[key]['stock']+=sumar
                    elif opcion == '2':
                        resta=int(input('Ingrese cantidad a restar: '))
                        self.stock[key]['stock']-=resta
                    elif opcion == '3':
                        print(f"Nombre: {self.stock[key]['nombre']}\nStock: {self.stock[key]['stock']}\nGuardado Correctamente")
                        break
                    else:
                        print("Ingrese opción valida...")   
                break


            except:
                print("Ingrese un producto existente")



