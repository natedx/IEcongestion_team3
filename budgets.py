#======= Constantes =======

    #=== Bus ===

capacite_bus=90         #personnes
prix_bus=250000         #€
conso_bus=25            #L/100km
v_bus=40                #km/h
entretien_bus=1500          #€/mois

    #=== Bus articule ===

capacite_articule=150   #personnes
prix_articule=280000    #€
conso_articule=35       #L/100km
v_articule=35           #km/h
entretien_articule=1500          #€/mois

    #=== Bus auto ===

capacite_bus_auto=80    #personnes
prix_bus_auto=400000    #€
conso_bus_auto=20       #L/100km
v_bus_auto=20           #km/h
entretien_bus_auto=1500          #€/mois

    #===taxi auto===

capacite_taxi=6         #personnes
prix_taxi=230000        #€
conso_taxi=15           #kWh/100km
v_taxi=40               #km/h
prix_batterie=50000     #€
periode_remplacement=27 #mois
prix_batterie_mois=prix_batterie/periode_remplacement
entretien_taxi=60      #€/mois

    #=== General===

salaire_chauffeur=4000  #€/mois
heures_mois=35*4.5
salaire_par_heures=salaire_chauffeur/heures_mois


prix_gazole=1.4         #€/L
prix_kWh=0.12           #€/kWh la nuit

duree_amortissement=15*12 #mois

duree_fonctionnement_normal=18       #h/jour
duree_fonctionnement_rush=5        #h/jour
duree_fonctionnement_moyen=14

#======= Fonctions =======

def cout_mois_capa(prix, conso, vitesse, entretien,capacite, n_heures, n_mois, auto=False, electrique=False):
    '''rertourne le prix sur n_mois, pour un bus qui tourne n_heures par jour compensé '''
    coef=capacite*vitesse*n_heures
    if not auto:
        salaire = salaire_par_heures * n_heures * 30
    else:
        salaire = 0
    if not electrique:
        consomation = prix_gazole * vitesse * n_heures / 100 * conso
    else:
        consomation=prix_kWh*vitesse*n_heures*conso/100
    return (prix/n_mois + salaire + consomation + entretien)/coef

def cout_unitaire_mois(prix, conso, vitesse, entretien, n_heures, n_mois, auto=False, electrique=False):
    '''rertourne le prix sur n_mois, pour un bus qui tourne n_heures par jour '''
    if not auto:
        salaire = salaire_par_heures * n_heures * 30
    else:
        salaire = 0
    if not electrique:
        consomation = prix_gazole * vitesse * n_heures / 100 * conso
    else:
        consomation=prix_kWh*vitesse*n_heures*conso/100
    return (prix / n_mois + salaire + consomation + entretien)

def cout_fonctionnement_mois(type):
    '''retourne les frais de fonctionements pour un moi par bus'''

    salaire=salaire = salaire_par_heures * duree_fonctionnement_normal * 30

    if type=='taxi':
        consomation=prix_kWh*v_taxi*duree_fonctionnement_normal*conso_taxi/100
        return consomation+entretien_taxi+prix_batterie_mois

    elif type=='bus':
        consomation = prix_gazole * v_bus * duree_fonctionnement_normal / 100 * conso_bus
        return salaire+consomation+entretien_bus

    elif type=='bus_auto':
        consomation = prix_gazole * v_bus_auto * duree_fonctionnement_normal / 100 * conso_bus_auto
        return consomation + entretien_bus_auto

    elif type=='bus_articule':
        consomation = prix_gazole * v_articule * duree_fonctionnement_normal / 100 * conso_articule
        return salaire + consomation + entretien_articule



def full_bus(budjet_max):
    nmax=budjet_max/cout_unitaire_mois(prix_bus, conso_bus, v_bus,entretien_bus, duree_fonctionnement_moyen, duree_amortissement)
    return int(nmax)

def full_articule(budjet_max):
    nmax=budjet_max/cout_unitaire_mois(prix_articule, conso_articule, v_articule, entretien_articule, duree_fonctionnement_moyen, duree_amortissement)
    return int(nmax)

def full_bus_auto(budjet_max):
    nmax=budjet_max/cout_unitaire_mois(prix_bus_auto, conso_bus_auto, v_bus_auto, entretien_bus_auto, duree_fonctionnement_moyen, duree_amortissement, auto=True)
    return int(nmax)

def full_taxi(budjet_max):
    nmax=budjet_max/cout_unitaire_mois(prix_taxi, conso_taxi, v_taxi, entretien_taxi+prix_batterie_mois, duree_fonctionnement_moyen, duree_amortissement, auto=True,electrique=True)

    return int(nmax)

def plot_comparison(normal=True, rush=True):
    import matplotlib.pyplot as plt
    import numpy as np

    t=np.array([x for x in range(2*12,15*12)])
    trucs_a_plot_normal={'normal_bus' : cout_mois_capa(prix_bus, conso_bus, v_bus ,entretien_bus, capacite_bus, duree_fonctionnement_normal, t),
                        'normal_articule' : cout_mois_capa(prix_articule, conso_articule, v_articule, entretien_articule, capacite_articule, duree_fonctionnement_normal, t),
                        'normal_bus_auto' : cout_mois_capa(prix_bus_auto, conso_bus_auto, v_bus_auto, entretien_bus_auto, capacite_bus_auto, duree_fonctionnement_normal, t, auto=True),
                        'normal_taxi' : cout_mois_capa(prix_taxi, conso_taxi, v_taxi, entretien_taxi+prix_batterie_mois, capacite_taxi, duree_fonctionnement_normal, t, auto=True, electrique=True)}

    trucs_a_plot_rush={'rush_bus' : cout_mois_capa(prix_bus, conso_bus, v_bus, entretien_bus, capacite_bus, duree_fonctionnement_rush, t),
                       'rush_articule': cout_mois_capa(prix_articule, conso_articule, v_articule, entretien_articule,capacite_articule, duree_fonctionnement_rush, t),
                       'rush_bus_auto': cout_mois_capa(prix_bus_auto, conso_bus_auto, v_bus_auto, entretien_bus_auto,capacite_bus_auto, duree_fonctionnement_rush, t, auto=True),
                       'rush_taxi': cout_mois_capa(prix_taxi, conso_taxi, v_taxi, entretien_taxi + prix_batterie_mois,capacite_taxi, duree_fonctionnement_rush, t, auto=True,electrique=True)}
    if normal:
        for truc in trucs_a_plot_normal:
            plt.plot(t,trucs_a_plot_normal[truc])
        plt.legend([truc for truc in trucs_a_plot_normal])

    if rush:
        for truc in trucs_a_plot_rush:
            plt.plot(t,trucs_a_plot_rush[truc])
        plt.legend([truc for truc in trucs_a_plot_rush])
    plt.grid()
    plt.xlabel('durée d\'amortissement (mois)')
    plt.ylabel('prix compensé (relatif)')
    plt.show()