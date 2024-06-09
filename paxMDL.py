from objecteSimulacio import *
from motorEventsDiscrets import *
import json
import random

class paxMDL(objecteSimulacio):
    darrer_estat=None
    def __init__(self, motor, parameters):
        super(paxMDL, self).__init__(motor, parameters)
        with open('paxMDL.cfg', 'r') as file:
            data_loaded = json.load(file)

        dades = data_loaded["Propietats"][self._nom]
        print(dades)

        self.temps = dades["temps"] # segons que el paio esta caminant cap on sigui 
        self.agafaTren = dades["agafaTren"]
        self.PMR = dades["PMR"]
        self.seguent = dades["seguent"]
        self.tipus = dades["tipus"]
        if self.tipus=="":
            self.tipus = "PMR"
        self.set_estat(Estat.ARRIBAT) 
    
    def __repr__(self):
        return self._nom
    
    def tractarEsdeveniment(self, event):
        #És molt habitual establir una primera selecció de l'estat en que em trobo i després fer una selecció de l'event
        self.darrer_estat=self._estat
        if (self.get_estat()==Estat.ANANT):
            if (event.tipus==TipusEvent.Arribada):
                self.processarArribadaLliure(event) 
                return
        pass     

    def processarArribadaLliure(self,event):
        
        delta= random.uniform((45*60) - self.temps, (5*60) - self.temps) # ho passo a segons (els paxs arriben o molt d'hora o tard :[ o entre mig tmb))
        self.programarEsdeveniment(delta,TipusEvent.Arribada,event.entitat,self.motor.donamObjecte(self.seguent))
        self.set_estat(Estat.ARRIBAT) # arriba a on sigui

    def iniciSimulacio(self):
        super(paxMDL, self).iniciSimulacio()
        #per simplificar exemple, considero que el meu successor serà un sol i que serà l'objecte amb _id=_id+1 
        self._successors=self.motor.donamObjecte(self._nom) #base 0 però identificador en base 1
        self.set_estat(Estat.ANANT)
         #Això és molt important recordar de poder fixar la llavor
        random.seed(5)

    def summary(self):
        stats = (
            f"Passatgers tipus {self.tipus}: {self.paxs_totals}\n"
            f"Passatgers que arriben tard: {self.paxs_tard}\n"
        )
        print(stats)
        return stats
        
    def trace(self,esdeveniment):
        return "Temps {} ".format(esdeveniment.tempsExecucio)+" "+str(self)+" a "+str(self.darrer_estat)+ " rep "+ str(esdeveniment.tipus)+" passa a "+str(self.get_estat()) 