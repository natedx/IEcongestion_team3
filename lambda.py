import matplotlib.pyplot as plt
import numpy as np

prix_bus=200000         #€
prix_articule=300000    #€
prix_bus_auto=400000   #€

conso_bus=25            #L/100km
conso_articule=35       #L/100km
conso_bus_auto=20       #L/100km

prix_gazole=1.4         #€/L

v_bus=40                #km/h
v_articule=35           #km/h
v_bus_auto=20           #km/h

salaire_chauffeur=4000  #€/mois
heures_mois=35*4.5

entretien=1500          #€/mois

capacite_bus=90         #personnes
capacite_articule=150   #personnes
capacite_bus_auto=80    #personnes

salaire_par_heures=salaire_chauffeur/heures_mois

def cout_mois_capa(prix, conso, capacite, vitesse, auto, n_heures, n_mois):
    '''rertourne le prix sur n_mois, pour un bus qui tourne n_heures par jour '''
    coef=capacite*vitesse*n_heures
    if not auto:
        salaire=salaire_par_heures*n_heures*30
    else:
        salaire=0
    petrole=prix_gazole*vitesse*n_heures/100*conso
    #print((salaire + petrole + entretien)/coef)
    return (prix/n_mois + salaire + petrole + entretien)/coef

h1=18       #h/jour
h2=5        #h/jour

t=np.array([x for x in range(5*12,20*12)])

l1_bus=cout_mois_capa(prix_bus, conso_bus, capacite_bus, v_bus, False,  h1, t)
l2_bus=cout_mois_capa(prix_bus, conso_bus, capacite_bus, v_bus, False, h2, t)

l1_articule=cout_mois_capa(prix_articule, conso_articule, capacite_articule, v_articule, False,  h1, t)
l2_articule=cout_mois_capa(prix_articule, conso_articule, capacite_articule, v_articule, False, h2, t)

l1_bus_auto=cout_mois_capa(prix_bus_auto, conso_bus_auto, capacite_bus_auto, v_bus_auto, True, h1, t)
l2_bus_auto=cout_mois_capa(prix_bus_auto, conso_bus_auto, capacite_bus_auto, v_bus_auto, True, h2, t)
plt.plot(t,l1_bus)
plt.plot(t,l2_bus)
plt.plot(t,l1_articule)
plt.plot(t,l2_articule)
plt.plot(t,l1_bus_auto)
plt.plot(t,l2_bus_auto)

plt.legend(['l1_bus','l2_bus','l1_articule','l2_articule','l1_bus_auto','l2_bus_auto'])
plt.show()