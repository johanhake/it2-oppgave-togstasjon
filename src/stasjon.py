class Stasjon:
    def __init__(self, navn):
        self.navn = navn
        self.lokomotiv = []

    def registrer_lokomotiv(self, lokomotiv):
        self.lokomotiv.append(lokomotiv)

    def registrer_pakke(self, pakke):
        for lok in self.lokomotiv:
            if lok.destinasjon == pakke.destinasjon:
                lok.registrer_pakke(pakke)
                return
        raise ValueError(f"Lok med destinasjon {pakke.destinasjon} ikke funnet")

class Togdel:
    def __init__(self, serienr, vekt, maksvekt):
        self.serienr = serienr
        self.vekt = vekt
        self.maksvekt = maksvekt

    def beregn_vekt(self):
        NotImplemented("Klassen Togdel må arves og beregn_vekt må implementers")

    def sjekk_vekt(self, vekt=.0):
        return self.beregn_vekt() + vekt <= self.maksvekt
    
class Lokomotiv(Togdel):
    def __init__(self, serienr, vekt, maksvekt, destinasjon):
        super().__init__(serienr, vekt, maksvekt)
        self.destinasjon = destinasjon
        self.vogner = []

    def beregn_vekt(self):
        return self.vekt + sum(vogn.beregn_vekt() for vogn in self.vogner)
    
    def registrer_vogn(self, vogn):
        if self.sjekk_vekt(vogn.beregn_vekt()):
            self.vogner.append(vogn)
            return  
        raise ValueError("Vognen er for tung. Den ble ikke registrert")
    
    def registrer_pakke(self, pakke):
        if self.sjekk_vekt(pakke.vekt):
            for vogn in self.vogner:
                if vogn.sjekk_vekt(pakke.vekt):
                    vogn.pakker.append(pakke)
                    return
        raise ValueError("Pakken er for tung. Den ble ikke registrert")

class Vogn(Togdel):
    def __init__(self, serienr, vekt, maksvekt):
        super().__init__(serienr, vekt, maksvekt)
        self.pakker = []

    def beregn_vekt(self):
        return self.vekt + sum(pakke.vekt for pakke in self.pakker)
    
class Pakke:
    def __init__(self, destinasjon, vekt, innhold):
        self.destinasjon = destinasjon
        self.vekt = vekt
        self.innhold = innhold
