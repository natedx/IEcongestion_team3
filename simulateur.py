#Tentative de simulation de l'acheminement de passagers

import numpy as np

#Variables décrivant le trajet suivi
l = 10 #longueur du trajet en km
v = 50 #vitesse du véhicule en km/h
n = 12 #nombres d'arrêts de la ligne
t = 1 #temps passé par le véhicule à chaque arrêt en h
t_trj = int(l/(v/60)+n*t) #temps d'une allée
capa = 60 #capacité d'un véhicule


d_simul = 120

table_p = np.zeros((1,d_simul))[0] #table qui va contenir le nombre de passagers en fonctions du temps sur une durée de 2h où l'intervalle de temps est de 1 min.

table_v = np.zeros((1,d_simul))[0] #table qui va contenir les véhicules présents à l'arrêt en fonction du temps.



def flux (t):
    """flux sera a priori une donnée du groupe 4
       Dans notre exemple nous prendrons un flux de 50 nouvelles personnes toutes les 10 
       minutes"""
    if t%10 == 0:
        return 50
    else:
        return 0

#mettons qu'on n'ait qu'un seul bus en position 0 initialement.

#Init
table_v[0] = 1



#Evolution du système

for i in range(0,d_simul-1):
    
    #On met à jour le nombre de passagers:
    table_p[i] += flux(i)
    
    #Si il y a un bus on charge un maximum de passagers
    if table_v[i] >= 1:
        table_v[i+1] += table_v[i]-1
        table_p[i+1] = max(table_p[i]-capa, 0)
        if i+t_trj < d_simul:
            table_v[i+t_trj] += 1
    else:
        table_p[i+1] += table_p[i]


print(table_p)
print(table_v)
        
    
    


















