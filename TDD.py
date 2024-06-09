from esdeveniment import *
from passatger import *
from tren import *
from motorEventsDiscrets import *
import random

'''
Podeu canviar el contingut de la funció de sota i així poder tenir el vostre propi banc de proves, no soc molt
de test així que us poso la versió cutre.
'''

def TDDMola(motor):
    pax=passatger()#el meu passatge, si necessita atributs doncs...
    pax.propietats["PMR"]=True #per exemple
    tog=tren()#si necessito un tren el tinc aquí (en noruec) però tampoc té atributs :(
    tog.propietats["pugen"]=100
    temps=0 #expressats en segons
    event=TipusEvent.Arribada
    elmeuobjecte=motor.donamObjecte("AV1")#està clar que AV1 és el nom del meu objecte
    for i in range(0,3):
        motor.donamObjecte("AV1").programarEsdeveniment(temps+i,event,pax,elmeuobjecte)

def TDDMola2(motor):
    
    hora_inici = 16
    tog=tren() #creo els paxs una hora abans de que arribi el tren !
    tog.propietats["pugen"]=100
    paxs_totals = 0
    paxs_tard = 0
    for j in range(0,8):
        temps=hora_inici*3600
        event=TipusEvent.Arribada
        elmeuobjecte=motor.donamObjecte("PA1")
        for i in range(0,10):
            delta= random.uniform(temps - (45*60),temps - (-5*60)) #paxs arriben entre 45 i 5 min abans de que surti el tren
            paxs_totals+=1
            if (delta > temps): 
                elmeuobjecte.sumar_pax_tard()
                paxs_tard+=1
            elmeuobjecte.sumar_pax()
            motor.donamObjecte("PA1").programarEsdeveniment(delta,event,tog,elmeuobjecte)
        elmeuobjecte=motor.donamObjecte("PA2")
        for i in range(0,45):
            delta= random.uniform(temps - (45*60),temps - (-5*60)) 
            paxs_totals+=1
            elmeuobjecte.sumar_pax()
            if (delta > temps): 
                elmeuobjecte.sumar_pax_tard()
            motor.donamObjecte("PA2").programarEsdeveniment(delta,event,tog,elmeuobjecte)
        elmeuobjecte=motor.donamObjecte("PA3")
        for i in range(0,45):
            delta= random.uniform(temps - (45*60),temps - (-5*60)) 
            paxs_totals+=1
            if (delta > temps): 
                elmeuobjecte.sumar_pax_tard()
            elmeuobjecte.sumar_pax()
            motor.donamObjecte("PA3").programarEsdeveniment(delta,event,tog,elmeuobjecte)
    
        hora_inici+=1

    