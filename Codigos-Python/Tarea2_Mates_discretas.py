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
    
    def anidar(self):
        '''
        # Obtener la lista de muñecas y el tamaño
        munieca = self.getMatryoshka()
        tam = self.getTamanio()
        
        if tam == len(munieca):
            for i, muneca_i in enumerate(munieca):
                munieca_s = muneca_i + 1
                if munieca_s in munieca:
                    indice_muñeca_i = munieca.index(muneca_i)
                    # Intercambiar las posiciones de las muñecas
                    munieca[indice_muñeca_i], munieca[indice_muñeca_i + 1] = munieca_s, muneca_i
        return munieca
        '''
        #munieca_s=muneca_i+1
        self.matryoshka = munieca
        munieca=self.getMatryoshka() #será la lista de muñecas
        tam= self.getTamanio()
        if tam==len(munieca):
            muneca_i=1
            for indice, muneca_i in enumerate(munieca[:]):
                munieca_s = muneca_i + 1
                if munieca_s in munieca:
                    indice_muñeca_i = munieca.index(muneca_i) 
                    munieca.pop(indice_muñeca_i)
        return munieca       
        
        

        
    


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
muñeca1.anidar()
#muñeca1.anidarRecursivo()


















