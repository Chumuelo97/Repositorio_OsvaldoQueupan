import random
import time

#Vamos a crear por mientras la clase muñeca
#Y los metodos 'anidar' y 'desanidar'

#imports que debemos tener:

#*para numeros random sin repetir

class Matryoshka(list):
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.matryoshka = None

        
    
    def anidar_recursivo(self, munieca):
        
        if len(munieca) == 0:
            return munieca #return munieca NONE       
        else:
            print(f"Orden de las muñecas (Recursivo): {munieca}")
            time.sleep(1)

            self.matryoshka = munieca
            muneca_i = min(munieca)
            munieca_s = max(munieca)

            indice_muneca_i = munieca.index(muneca_i)
            indice_muneca_s = munieca.index(munieca_s)

            munieca.pop(indice_muneca_i)
            muneca_i = munieca_s

            return self.anidar_recursivo(munieca)

    def anidar_iterativo(self, munieca):
        while len(munieca) > 0:
            print(f"Orden de las muñecas (Iterativo): {munieca}")
            time.sleep(1)

            self.matryoshka = munieca
            muneca_i = min(munieca)
            muneca_s = max(munieca)

            indice_muneca_i = munieca.index(muneca_i)
            indice_muneca_s = munieca.index(muneca_s)

            munieca.pop(indice_muneca_i)
            muneca_i = muneca_s

        return self.anidar_recursivo(munieca)   
    

    def desanidar(self,munieca):
         
        self.anidar_iterativo=munieca
        lista=[]
        #creamos una estructura iterativa
        for i in munieca:
            lista.append(i)
        #creamos una lista ordenada
        lista_o = sorted(lista, reverse=True)
        for j in lista_o:
            print(f"Desanidación: {j}")
        return lista 

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
        return m_list
        


muñeca1= Matryoshka(0)
muñeca1.getTamanio() 
munieca_inicial = muñeca1.getMatryoshka() 
# Versión Recursiva
start_time_recursivo = time.time()
muñeca_anidada_recursivo = muñeca1.anidar_recursivo(munieca_inicial.copy())
end_time_recursivo = time.time()
 

# Versión Iterativa con copia de la lista
start_time_iterativo = time.time()
muñeca_anidada_iterativo = muñeca1.anidar_iterativo(munieca_inicial.copy())
end_time_iterativo = time.time()

# Versión desanidar
start_time_desanidar = time.time()
muñeca_desanidada = muñeca1.desanidar(munieca_inicial)
end_time_desanidar = time.time()



print(f"Tiempo de ejecución (Recursivo): {end_time_recursivo - start_time_recursivo} segundos")
print(f"Tiempo de ejecución (Iterativo): {end_time_iterativo - start_time_iterativo} segundos")
print(f"Tiempo de ejecución (Anidar): {end_time_desanidar - start_time_desanidar} segundos")















