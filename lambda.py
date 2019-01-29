import matplotlib.pyplot as plt
import numpy as np


#======= Constantes =======

    #=== Bus ===

capacite_bus=90         #personnes
prix_bus=200000         #€
conso_bus=25            #L/100km
v_bus=40                #km/h

    #=== Bus articule ===

capacite_articule=150   #personnes
prix_articule=300000    #€
conso_articule=35       #L/100km
v_articule=35           #km/h

    #=== Bus auto ===

capacite_bus_auto=80    #personnes
prix_bus_auto=400000    #€
conso_bus_auto=20       #L/100km
v_bus_auto=20           #km/h

    #=== General===

salaire_chauffeur=4000  #€/mois
heures_mois=35*4.5
salaire_par_heures=salaire_chauffeur/heures_mois

entretien=1500          #€/mois
prix_gazole=1.4         #€/L

duree_amortissement=15*12 #mois

duree_fonctionnement_normal=18       #h/jour
duree_fonctionnement_rush=5        #h/jour
duree_fonctionnement_moyen=10
#======= Fonctions =======

def cout_mois_capa(prix, conso, capacite, vitesse, auto, n_heures, n_mois):
    '''rertourne le prix sur n_mois, pour un bus qui tourne n_heures par jour compensé '''
    coef=capacite*vitesse*n_heures
    if not auto:
        salaire=salaire_par_heures*n_heures*30
    else:
        salaire=0
    petrole=prix_gazole*vitesse*n_heures/100*conso
    return (prix/n_mois + salaire + petrole + entretien)/coef

def cout_unitaire_mois(prix, conso, vitesse, auto, n_heures, n_mois):
    '''rertourne le prix sur n_mois, pour un bus qui tourne n_heures par jour '''
    if not auto:
        salaire = salaire_par_heures * n_heures * 30
    else:
        salaire = 0
    petrole = prix_gazole * vitesse * n_heures / 100 * conso
    return (prix / n_mois + salaire + petrole + entretien)

def full_bus(budjet_max, flux, temps_arret):
    nmax=budjet_max/cout_unitaire_mois(prix_bus, conso_bus, v_bus, False, duree_fonctionnement_moyen, duree_amortissement)
    return nmax



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