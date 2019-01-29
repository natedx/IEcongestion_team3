#Tentative de simulation de l'acheminement de passagers

import numpy as np


def flux_test (t):
    """flux sera a priori une donnée du groupe 4
       Dans notre exemple nous prendrons un flux de 50 nouvelles personnes toutes les 10 
       minutes"""
    if t%10 == 0:
        return 50
    else:
        return 0

def non_nul(table):
    i = len(table)-1
    while i>= 0 and table[i] == 0:
        i -= 1
    return i

    
    
def simul(init,cout,flux,longueur,vitesse,nb_arret,t_arret,capa,d_simul):
    """
    Cette fonction permet de calculer les tables d'évolution des passagers en attente
    et les tables de disponibilité des bus.
    Variables:
    init        --  initialisation des position des bus sous forme de liste de liste
                    exemple: init = [(0,1), (5,1), (10,1)]
    cout        --  cout
    flux        --  flux d'arrivé des passagers
    longueur    --  longueur du trajet en km
    vitesse     --  vitesse moyenne du véhicule en km/h
    nb_arret    --  nombre d'arrêts sur la ligne
    t_arret     --  temps moyen passé à un arrêt en min
    capa        --  capacité d'un véhicule
    d_simul     --  durée de la simulation en min
    """
    #Calcul du temps de trajet:
    t_trj = int(longueur/(vitesse/60)+nb_arret*t_arret)
    
    attentes = [0 for i in range(d_simul)]
    moyenne = []
    
    #Initialisation des tables d'évolution
    table_p = np.zeros((1,d_simul))[0]
    table_v = np.zeros((1,d_simul))[0]

    
    #Initialisation des véhicules:
    for (i, nb) in init:
        table_v[i] = nb
    
    #Evolution du système
    for i in range(0,d_simul-1):
        
        for j in range(d_simul-1, 0, -1):
            attentes[j] = attentes[j-1]
        attentes[0] = flux(i)
        nb_bus_i = table_v[i]
        if nb_bus_i != 0:
            nb_personnes_montant = int(nb_bus_i*capa)
            maxi = non_nul(attentes)
            while nb_personnes_montant > 0 and maxi >= 0:
                if attentes[maxi] >= nb_personnes_montant:
                    attentes[maxi] += -(nb_personnes_montant)
                    for k in range(nb_personnes_montant):
                        moyenne += [maxi]
                        nb_personnes_montant = 0
                        break
                if attentes[maxi] < nb_personnes_montant:
                    for k in range(attentes[maxi]):
                        moyenne += [maxi]
                    nb_personnes_montant = nb_personnes_montant - attentes[maxi]
                    attentes[maxi] = 0
                    maxi = maxi-1
        
        #On met à jour le nombre de passagers à la minute i
        table_p[i] += flux(i)
        
        #Si il y a un bus
        if table_v[i] >= 1:
            #On suppose qu'au plus un bus part par minute
            table_v[i+1] += table_v[i]-1
            #On charge un maximum de passagers
            table_p[i+1] = max(table_p[i]-capa, 0)
            #Il y aura donc un nouveau bus à i+2*t_trj
            if i+2*t_trj < d_simul:
                table_v[i+2*t_trj] += 1
                
        #S'il n'y a pas de bus, les passagers sont encore là à i+1
        else:
            table_p[i+1] += table_p[i]
    
    return table_p, table_v, moyenne
    
    
    
    
    

def test():
    init = [(0,1), (5,1), (10,1)]
    flux = flux_test
    longueur = 10 #longueur du trajet en km
    vitesse = 50 #vitesse du véhicule en km/h
    nb_arret = 12 #nombres d'arrêts de la ligne
    t_arret = 1 #temps passé par le véhicule à chaque arrêt en h
    capa = 60
    d_simul = 120
    cout = 0
    table_v, table_p,moyenne = simul(init,cout,flux,longueur,vitesse,nb_arret,t_arret,capa,d_simul)
    print(table_v,table_p,moyenne, np.average(moyenne), sep ='\n')
    














