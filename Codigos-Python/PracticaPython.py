#Aquí vamos a proceder a realizar ejemplos en python con el paradigma POO
#A ver que sale xdxdxd

'''
Como debe ser declarado una clase:

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

    #creamos otro metodo que será el metodo:
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

'''


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
