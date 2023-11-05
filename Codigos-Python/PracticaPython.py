#Aquí vamos a proceder a realizar ejemplos en python con el paradigma POO
#A ver que sale xdxdxd

#Que es una clase en Python:

#Como debe ser declarado una clase:
'''
Class Nombredelaclase (object): #Declaramos la clase nuestra que hereda de Object

      def  __init__ (self, parámetros): #Constructor de la clase

#Declaración de atributos

En java es un constructor:

public nombreConstructor(parametros que son los atributos con sus respectivos tipos de datos) {
    nombre_atributo1= algun caracter que se asigne para el atributo;
    nombre_atributo2= algun caracter que se asigne para el atributo;
    nombre_atributo3= algun caracter que se asigne para el atributo;
}




#primero lo primero, crearemos una clase llamada Humano
class Humano():
    #definimos el método constructor pero no es necesario que exita de por si
    # este metodo va a inicializar los atributos del objeto creado a partir de la clase que
    # lo posea. 
    # 'def' <-- es para inicializar una función o método en este caso!
    def __init__(self, edad, nombre, ocupacion): #atributos de la clase Humano.
        self.edad= edad
        self.nommbre= nombre
        self.ocupacion=ocupacion
    
    #creamos nuestro metodo:
    def presentar(self):
        presentacion=("Hola! Soy {}, mi edad es {} y mi ocupacion es {}")
        print(presentacion.format(self.nommbre, self.edad, self.ocupacion))

    #creamos otro metodo, que será el metodo contratar:
    def contratar(self, puesto):
        self.puesto=puesto
        print("{} ha sido contratado como {}".format(self.nommbre,self.puesto))
        self.ocupacion=puesto

#instanciando un objeto:
Persona1= Humano(31, "Osvaldo", "cualquier pega oe") 
Persona1.presentar()
Persona1.contratar("Ingeniero")
print("Actualizando CV!\n")
Persona1.presentar()




#Vamos a progaramar un autito, crear su clase y objeto

#creamos la clase Auto
class Auto():
    #creamos el constructor con los atributos
    def __init__(self, patente, marca, anho):
        self.patente=patente
        self.marca=marca
        self.anho=anho
    
    #creamos sus metodos
    def Actualiza_marca(self,marca_auto):
        self.marca_auto=marca_auto
        print("ingrese una marca:\n")
        self.marca_auto=input()
        print("**Datos actualizados**")
        #print("patente: {}\n nueva marca: {}\n anho: {}\n".format(self.patente,self.marca_auto,self.anho))
        self.marca=self.marca_auto
    
    def mostrarDatos(self):
        print("Datos del auto:\n")
        print("patente: {}\n marca: {}\n anho: {}\n".format(self.patente,self.marca,self.anho))

Car1= Auto("XX-XXX-XXx","suvaru", 2023)

Car1.mostrarDatos()
Car1.Actualiza_marca("marca_auto")#'marca_auto' es el argumento que se espera para poder ingresar por teclado el nombre de la marca nueva de nuestro auto, 
                                             #seguirá teniendo mismo anho y misma patente pero se actualiza la marca en este caso. 

Car1.mostrarDatos()#Mostrará los datos actualizados


class Botella_agua(object):

    def __init__(self, marca, litros, tipo):
        self.marca=marca
        self.litros=litros
        self.tipo=tipo
    
    def datos(self):
        print("ingrese datos para la botella de agua:")
        self.marca=input("marca:")
        self.litros=input("litros:")
        self.tipo=input("tipo de agua:")
        print("\n")
        print("Datos de la botella es:")
        print("marca: {}\n litros: {}\n tipo de agua: {}\n".format(self.marca,self.litros,self.tipo))

Agua1=Botella_agua("","","")
Agua1.datos()


#HERENCIA SIMPLE

#procedemos a crear 2 clases
#Existe clase padre y la clase hija
#veremos un ejemplo con estudiante y su carrera

class Estudiante():
    #inicializamos el constructor
    def __init__(self, edad, nombre):
        self.nombre=nombre
        self.edad=edad

class Carrera(Estudiante):#<---- esto será la clase hija que va heredad todos los atributos de la clase padre
    
    def presentar(self):
        print(f"Hola soy {self.nombre} tengo {self.edad} y estudio una carrera. ")#<--- esto es una cadena de formato, por eso se utiliza el 'f'



Osvaldo= Carrera(26, 'Osvaldo Queupán') #<--- le asignamos al objeto 'Osvaldo' la clase 'Carrera'
Osvaldo.presentar()

#HERENCIA MULTIPLE

class Estudiante():  #clase padre 1
    #inicializamos el constructor
    def __init__(self, edad, nombre):
        self.nombre=nombre
        self.edad=edad

class Instituto(): #clase padre 2
    def presentarI(self):
        print("Estudio en una universidad jejeje")

class Carrera(Estudiante, Instituto):#<---- esto será la clase hija que va heredad todos los atributos de la clase padre
    
    def presentar(self):
        print(f"Hola soy {self.nombre} tengo {self.edad} y estudio una carrera. ")#<--- esto es una cadena de formato, por eso se utiliza el 'f'



Osvaldo= Carrera(26, 'Osvaldo Queupán') #<--- le asignamos al objeto 'Osvaldo' la clase 'Carrera'
Osvaldo.presentar()
Osvaldo.presentarI()

#Nota: El objeto 'Osvaldo' de la clase 'Carrera' puede tomar los metodos de las otras clases
       #ya que hereda de la clase 'Estudiante' y de la clase 'Instituto'.
       #Además podemos decir que la Herencia Multiple es como formar una familia,
       #Una madre, un padre como clases principales y un hijo como clase secundaria o hija
       #Heredará los métodos y atributos de las clases padres.



#Funcion super()


class AgregarElemento(list):
    def append(self, alumno): #'alumno' es un parametro dentro de la clase padre
        print(("Nombre del bro agregado: "), (alumno))
        super().append(alumno) 

Lista1= AgregarElemento()
Lista1.append("osvaldo")
print(Lista1)

#Nota: la funcion 'super()' va a ser que herede el metodo 'append()' de la clase 
#padre 'List', lo cual la funcion 'super()' permite que se hereden (desde la clase padre)
#metodos y atributos sin especificar el nombre de la clase padre,
#ya que el nombre de esta está sujeto a cambios de nombres.


#funcion super en herencia multiple
class Perro(object):
    def ladrar(self):
        print("wau, wau,xd")

    def grunir(self):
        print("grrr, grrr")

class Caniche(Perro):
    def ladrar(self):
        print("wau, wau")

    def grunir(self):
        print("grrr, grrr")

class Pastor_Aleman(Perro):
    def ladrar1(self):
        print("wau, wau, wau")

    def grunir(self):
        print("grrr, grrr")

class Sheapoodle(Pastor_Aleman, Caniche):
    def contador_ladridos(self, cont):
        for i in range (cont):
            super(Sheapoodle, self).ladrar()
            

    def grunir(self):
        print("grrr, grrr")


Sheapoodle1= Sheapoodle()
Sheapoodle1.contador_ladridos(1)



#mates discretas:

import random

Vamos a crear por mientras la clase muñeca
Y los metodos 'anidar' y 'desanidar'

imports que debemos tener:

*para numeros random sin repetir

#
class Matryoshka(list):
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.matryoshka = None

    def anidar(self, munieca):
        
        self.matryoshka = munieca
        #meter las muñecas de menor tamaño a la muñeca de mayor tamaño que la de menor tamaño
        #va a generar la lista segun el tamaño de esta, tiene que generar las muñecas
        #va a recorrer la lista que se generó y si el tamaño de la muñeca es menor a la siguiente
        def buscar_elemento(lista):
            posiciones = []
            for i, valor in enumerate(lista):
                if valor == num_min:
                    posiciones.append(i)
            return posiciones

        num_min = 1
        # Solicitar al usuario el número de elementos de la lista
        num_elementos = int(input("Ingrese el número de elementos de la lista: "))

        # Generar una lista de números aleatorios no repetidos
        mi_lista = random.sample(range(num_min, num_elementos+1), num_elementos)

        print(f"Lista generada: {mi_lista}")

        posiciones = buscar_elemento(mi_lista)

        print(f"El elemento {num_min} se encuentra en las posiciones: {posiciones}")




    def getTamanio(self):
        return self.tamanio

    def getMatryoshka(self):
        return self.matryoshka

#proceso de 'anidar'

num_min = 1
num_sig=num_min+1

def buscar_elemento(lista):
    posiciones=[]
    for i, valor in enumerate(lista):
        if valor == num_min:
            posiciones.append(i)
    print(f"El numero {num_min} se encuentra en las posiciones: {posiciones}")
    return posiciones

def buscar_num_sig(lista):
    posiciones=[]
    for i, valor in enumerate(lista):
        if valor==num_sig:
            posiciones.append(i)
    print(f"El numero {num_sig} se encuentra en la posicion: {posiciones}")
    return posiciones

#crear una funcion que dado a que encontramos el indice del sucesor de num_min, actualice ese sucesor 
#como num_min, eliminando así el num_min y se actualiza la posicion del nuevo num_min y la lista  

def list_update(lista, num_min, num_sig):
    pos=[]
    indice_num_min = lista.index(num_min)
    for i,valor in enumerate(lista[:]):
        if valor==num_sig:
            lista.pop(indice_num_min)
            #ahora actualizamos el valor minimo y su indice o posicion
            num_min=num_sig
            pos.append(i)
            print(f"mi lista actualizada es{lista}")
            print(f"El numero {num_min} se encuentra en las posiciones: {pos}")
    return lista 

#Solicitar al usuario el número de elementos de la lista
num_elementos = int(input("Ingrese el número de elementos de la lista: "))

#Generar una lista de números aleatorios no repetidos
mi_lista = random.sample(range(num_min, num_elementos+1), num_elementos)

print(f"Lista generada: {mi_lista}")

posiciones = buscar_elemento(mi_lista)
#ahora buscaremos la posicion del sucesor del numero minimo

posiciones=buscar_num_sig(mi_lista)

mi_lista=list_update(mi_lista, num_min, num_sig)
#print(f"El numero actualizado como minimo es: {num_sig} se encuentra en la posicion: {posiciones}")


#y cuando lo encontremos, debemos actualizar el numero minimo eliminando de la lista el numero minimo pasado

#debemos guardar la posicion del numero minimo actualizado y buscar el otro numero que es el
#sucesor del pivote -> pivote = numero minimo actual


















def algoritmo_recursivo(matryoshka):
    if matryoshka.getMatryoshka() is not None:
        algoritmo_recursivo(matryoshka.getMatryoshka())
    print(matryoshka.getTamanio(), end=" ")

def algoritmo_iterativo(matryoshkas):
    for matryoshka in matryoshkas:
        print(matryoshka.getTamanio(), end=" ")

def algoritmo_desanidar(matryoshka):
    if matryoshka.getMatryoshka() is not None:
        algoritmo_desanidar(matryoshka.getMatryoshka())
    print(matryoshka.getTamanio(), end=" ")


#Input del usuario
N = int(input("Ingrese la cantidad de muñecas (N): "))
muñecas = generar_muñecas(N)

#Imprimir array creado al inicio
print("Array de muñecas:", [muñeca.getTamanio() for muñeca in muñecas])

#Algoritmo recursivo
start_time = time.time()
algoritmo_recursivo(muñecas[0])
print("\nTiempo de ejecución recursivo: %s segundos" % (time.time() - start_time))

#Algoritmo iterativo
start_time = time.time()
algoritmo_iterativo(muñecas)
print("\nTiempo de ejecución iterativo: %s segundos" % (time.time() - start_time))

#Algoritmo desanidar
start_time = time.time()
algoritmo_desanidar(muñecas[0])
print("\nTiempo de ejecución desanidar: %s segundos" % (time.time() - start_time))


    #obtiene el tamaño de la matryoshka
    def getTamanio(self):
        self.tamanio= int(input("Ingrese el número muñecas: "))
        return self.tamanio
    
     
    #obtiene la matryoshka almacenada 
    def getMatryoshka(self):
        #m_list es la lista que contienen las muñecas
        m_list = random.sample(range(1, self.tamanio+1), self.tamanio)
        self.matryoshka=m_list
        print(f"{m_list}")
        return self.matryoshka

'''


import random
import time
class Matryoshka:
    def init(self, tamanio):
        self.tamanio = tamanio #tamanio de la matryoshka
        self.matryoshka = None #almacena una matryoshka en el interior, valor None por defecto, ya que en un comienzo no hay matryoshkas en el interior

    #coloca una matryoshka dentro de otra
    def anidar(self, munieca):
        if munieca.tamanio < self.tamanio:
            self.matryoshka = munieca
        else:
            print("La muñeca es demasiado grande para anidarla.")

    #obtiene el tamaño de la matryoshka
    def getTamanio(self):
        return self.tamanio

    def anidar(self, muniecas):
        if not muniecas:
            return
        munieca = muniecas.pop(0)
        if munieca.tamanio < self.tamanio:
            self.matryoshka = munieca
            print(f"{self.tamanio} <--- {munieca.tamanio} ")
            self.matryoshka.anidar(muniecas)
        else:
            print("La muñeca es demasiado grande para anidarla.")
    #contar matrushkas
    def contarMatryoshkas(self):
        if self.matryoshka is None:
            return 0
        else:
            return 1 + self.matryoshka.contarMatryoshkas()
    #obtiene la matryoshka almacenada
    def getMatryoshka(self):
        return self.matryoshka


#Crear algunas muñecas Matryoshka de diferentes tamaños
start_time = time.time()
matryoshkas = [Matryoshka(i) for i in range(10, 0, -1)]
matryoshkas[0].anidar(matryoshkas[1:])
print(matryoshkas[0].contarMatryoshkas())
end_time = time.time()
execution_time = end_time - start_time
print("Tiempo de ejecución: ", execution_time)
