# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:53:18 2019

@author: leonardo.patino
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dataset.csv',delimiter=';')


lete    = ctrl.Antecedent(np.arange(0, 130, 1), 'lete')
leve    = ctrl.Antecedent(np.arange(0, 130, 1), 'leve')
le      = ctrl.Antecedent(np.arange(0, 130, 1), 'le')
te      = ctrl.Antecedent(np.arange(0, 130, 1), 'te')
ve      = ctrl.Antecedent(np.arange(0, 130, 1), 've')
ld      = ctrl.Antecedent(np.arange(0, 130, 1), 'ld')
vt      = ctrl.Antecedent(np.arange(0, 130, 1), 'vt')
td      = ctrl.Antecedent(np.arange(0, 130, 1), 'td')
vd      = ctrl.Antecedent(np.arange(0, 130, 1), 'vd')

alerta  = ctrl.Consequent(np.arange(0, 130, 1), 'alerta')


lete['bajo']     = fuzz.pimf(lete.universe, 10, 30, 50, 80)
lete['medio']    = fuzz.pimf(lete.universe, 20, 40, 60, 90)
lete['alto']     = fuzz.pimf(lete.universe, 30, 60, 80, 130)

leve['bajo']     = fuzz.pimf(leve.universe, 30, 50, 80, 90)
leve['medio']    = fuzz.pimf(leve.universe, 40, 60, 100, 110)
leve['alto']     = fuzz.pimf(leve.universe, 50, 70, 120, 130)

le['bajo']       = fuzz.pimf(le.universe, 0, 10, 20, 30)
le['medio']      = fuzz.pimf(le.universe, 10, 30, 50, 60)
le['alto']       = fuzz.pimf(le.universe, 20, 80, 90, 130)

te['bajo']       = fuzz.pimf(te.universe, 0, 10, 50, 60)
te['medio']      = fuzz.pimf(te.universe, 10, 20, 100, 120)
te['alto']       = fuzz.pimf(te.universe, 20, 40, 120, 130)

ve['bajo']       = fuzz.pimf(ve.universe, 0, 10, 20, 30)
ve['medio']      = fuzz.pimf(ve.universe, 10, 20, 30, 40)
ve['alto']       = fuzz.pimf(ve.universe, 30, 80, 90, 130)

ld['bajo']       = fuzz.pimf(ld.universe, 0, 5, 10, 15)
ld['medio']      = fuzz.pimf(ld.universe, 5, 10, 15, 30)
ld['alto']       = fuzz.pimf(ld.universe, 12, 15, 30, 60)

vt['bajo']       = fuzz.pimf(vt.universe, 0, 10, 20, 30)
vt['medio']      = fuzz.pimf(vt.universe, 10, 30, 50, 70)
vt['alto']       = fuzz.pimf(vt.universe, 20, 60, 110, 130)

td['bajo']       = fuzz.pimf(td.universe, 0, 1, 2, 3)
td['medio']      = fuzz.pimf(td.universe, 2, 3, 4, 5)
td['alto']       = fuzz.pimf(td.universe, 8, 15, 30, 60)

vd['bajo']       = fuzz.pimf(vd.universe, 0, 10, 20, 30)
vd['medio']      = fuzz.pimf(vd.universe, 40, 50, 60, 70)
vd['alto']       = fuzz.pimf(vd.universe, 50, 80, 90, 130)

alerta['verde']      = fuzz.pimf(alerta.universe, 0, 10, 20, 30)
alerta['amarillo']   = fuzz.pimf(alerta.universe, 10, 20, 30, 40)
alerta['naranja']    = fuzz.pimf(alerta.universe, 70, 80, 90, 130)

lete.view()
leve.view()
le.view()
te.view()
ve.view()
ld.view()
vt.view()
td.view()
vd.view()

"""
Fuzzy rules
-----------

Ahora, para hacer que estos triángulos sean útiles, definimos la * relación difusa *
entre variables de entrada y salida. Para los propósitos de nuestro ejemplo, considere
siete reglas simples:

si lete alto entonces alerta naranja
si leve alto entonces alerta naranja
si le alto entonces alerta verde
si te alto entonces alerta amarilla
si ve alto entonces alerta verde
si vd ó td alto entonces alerta verde

"""

#reglas
regla1 = ctrl.Rule(lete['alto'], alerta['naranja'])
regla2 = ctrl.Rule(leve['alto'], alerta['naranja'])
regla3 = ctrl.Rule(le['alto'], alerta['verde'])
regla4 = ctrl.Rule(te['alto'], alerta['amarillo'])
regla5 = ctrl.Rule(ve['alto'], alerta['verde'])
regla6 = ctrl.Rule(vd['alto']  | td['alto'], alerta['verde'])

# Cria um sistema de controle e uma simulação
alerta_ctrl = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6])
alerta_sim = ctrl.ControlSystemSimulation(alerta_ctrl)

"""
# Entrada test
alerta_sim.input['lete'] = 10
alerta_sim.input['leve'] = 15
alerta_sim.input['le']   = 2
alerta_sim.input['te']   = 20
alerta_sim.input['ve']   = 25
alerta_sim.input['vd']   = 4
alerta_sim.input['td']   = 30

# Calcula
alerta_sim.compute()
alerta_sim.output
alerta.view(sim=alerta_sim)
"""

def ic(param_alerta):
   # Entrada
   alerta_sim.input['lete'] = param_alerta[0]
   alerta_sim.input['leve'] = param_alerta[1]
   alerta_sim.input['le']   = param_alerta[2]
   alerta_sim.input['te']   = param_alerta[3]
   alerta_sim.input['ve']   = param_alerta[4]
   alerta_sim.input['vd']   = param_alerta[5]
   alerta_sim.input['td']   = param_alerta[6]

   # Calcula
   alerta_sim.compute()
   return(alerta_sim.output['alerta'])


def proceso(debug=False):
    fila = 0 
    #n = len(df)
    n = 100

    while fila < n:
        alerta_ = ic([df.iloc[fila, 6],df.iloc[fila, 7],df.iloc[fila, 8],df.iloc[fila, 9],df.iloc[fila, 10],df.iloc[fila, 11],df.iloc[fila, 12]])
        if df.iloc[fila, 5] != 'na':
            print("Intervalo: %s Alerta: %s" % (df.iloc[fila, 1], alerta_))
        if debug == True:
            alerta_sim.compute()    
            alerta_sim.output
            alerta.view(sim=alerta_sim)
        fila = fila + 1

#pasarle debug=True para ver las graficas en cada interación
proceso()

