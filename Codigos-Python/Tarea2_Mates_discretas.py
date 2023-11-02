import random


#Vamos a crear por mientras la clase muñeca
#Y los metodos 'anidar' y 'desanidar'

#imports que debemos tener:

#*para numeros random sin repetir

class Matryoshka(list):
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.matryoshka = None

    #se debe repetir el proceso
    #tamño de la lista= tam
    #la lista= lista
    #definir 
    # muñeca_i=1
    # muñeca_s=muñeca_i+1
    def anidar(self, munieca):
        muneca_i=1
        munieca_s=muneca_i+1
        self.matryoshka = munieca
        munieca=self.getMatryoshka() #será la lista de muñecas
        tam= self.getTamanio()

        for muneca_i in range(len(munieca)):
            if munieca==tam:
                indice_muñeca_i = munieca.index(muneca_i) 
                for i, valor in enumerate(munieca[:]):
                    i=indice_muñeca_i
                    if valor == munieca_s:
                        munieca.pop(i)
                        muneca_i=munieca_s
                        print(f"{munieca-1}")   
        return munieca         
            

         
            #for i in rango(lista):
            #    if cantidademuñecas == tamañodelalista:
            #        indice_muñeca_i = lista.index(muñeca_i)
            #        for i,valor in enumerate(lista[:]):
            #            if valor == muñeca_s:
            #                lista.pop(indice_muñeca_i)
            #                muñeca_i=muñeca_s 
            #return lista
        
            
       
        '''
        #crear una funcion que dado a que encontramos el indice del sucesor de num_min, actualice ese sucesor 
        #como num_min, eliminando así el num_min y se actualiza la posicion del nuevo num_min y la lista  
        num_min = 1
        num_sig=num_min+1
        def actualizar_lista(lista, num_min, num_sig):
            
            
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

        #posiciones = buscar_elemento(mi_lista)
        #ahora buscaremos la posicion del sucesor del numero minimo

        #posiciones=buscar_num_sig(mi_lista)

        mi_lista=actualizar_lista(mi_lista, num_min, num_sig)
     '''   
    


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


muñeca1= Matryoshka(0)
muñeca1.getTamanio()
muñeca1.getMatryoshka()
muñeca1.anidar(0)
#muñeca1.anidarRecursivo()


















