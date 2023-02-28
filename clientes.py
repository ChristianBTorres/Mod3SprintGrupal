import time
import random
class Clientes():
    def __init__(self): #Crear Clientes
        self.usuarios = {random.randint(10000,99999):{'nombre':'Cliente1', 'apellido':'Apellido1','edad': 23,'password':'contraseña1'}, 
                      random.randint(10000,99999):{'nombre':'Cliente2', 'apellido':'Apellido2','edad': 33,'password':'contraseña2'}, 
                      random.randint(10000,99999):{'nombre':'Cliente3', 'apellido':'Apellido3','edad': 44,'password':'contraseña3'}, 
                      random.randint(10000,99999):{'nombre':'Cliente4', 'apellido':'Apellido4','edad': 55,'password':'contraseña4'}}

    def menu(self):
        while True: 
            opcion = input("1.- Agregar Clientes \n2.- Eliminar Clientes \n3.- Listar Clientes\n4.- Salir\n>")
            if opcion == '1':
                self.agregar()
            elif opcion == '2':
                self.eliminar()
            elif opcion == '3':
                self.listar()  
            elif opcion == '4':
                print("EXIT")
                break
            else:
                print("Seleccione una opción válida...")


    def agregar(self): #Agregar nuevo cliente
        while True:
            id = random.randint(10000,99999) #Crear id aleatorio
            if id not in self.usuarios: #Validar que el id no exista en el diccionario
                nombre = input("Ingrese Nombre de Usuario\n")
                apellido = input("Ingrese Apellido\n")
                edad = (int(input("Ingrese edad: \n")))
                password = input("Ingrese su Contreña")
                self.usuarios[id]={'nombre':nombre, 'apellido':apellido,'edad':edad,'password':password}
                break

    def listar(self):
        for keys in self.usuarios:
            print("ID:" ,keys,"\nNombre:" ,self.usuarios[keys]['nombre'],"\nApellido:" ,self.usuarios[keys]['apellido'],"\nEdad:" ,self.usuarios[keys]['edad'])
            time.sleep(1)

    def eliminar(self):
        while True:
            key = input("Ingrese ID del Cliente que desea eliminar: ")
            try:
                key = int(key)
                del self.usuarios[key]
                break
            except:
                print("Ingrese un Cliente Existente.")

    



