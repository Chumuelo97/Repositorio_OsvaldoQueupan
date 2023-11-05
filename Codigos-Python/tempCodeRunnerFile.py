    tam = self.getTamanio()
        
        if tam == len(munieca):
            for i, muneca_i in enumerate(munieca):
                munieca_s = muneca_i + 1
                if munieca_s in munieca:
                    indice_muñeca_i = munieca.index(muneca_i)
                    indice_muñeca_s = munieca.index(munieca_s)
                    # Eliminar la muñeca actual y hacer que la siguiente sea la inicial
                    munieca.pop(indice_muñeca_i)
                    munieca.insert(indice_muñeca_i, muneca_s)
        return munieca