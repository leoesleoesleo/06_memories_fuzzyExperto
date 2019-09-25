# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:35:07 2019

@author: leonardo.patino
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# Los nuevos objetos antecedentes / consecuentes contienen variables del universo y pertenencia
# funciones
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# La función de membresía automática es posible con .automf (3, 5 o 7)
quality.automf(3)
service.automf(3)


# Las funciones de membresía personalizadas se pueden construir interactivamente con un familiar,
# Pythonic API
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

"""
To help understand what the membership looks like, use the ``view`` methods.
"""

# Puedes ver cómo se ven con .view()
quality['average'].view()
"""
.. image:: PLOT2RST.current_figure
"""
service.view()
"""
.. image:: PLOT2RST.current_figure
"""
tip.view()
"""
.. image:: PLOT2RST.current_figure


Fuzzy rules
-----------

Ahora, para hacer que estos triángulos sean útiles, definimos la * relación difusa *
entre variables de entrada y salida. Para los propósitos de nuestro ejemplo, considere
tres reglas simples:

1. Si la comida es mala O el servicio es pobre, entonces la propina será baja
2. Si el servicio es promedio, la propina será media
3. Si la comida es buena O el servicio es bueno, entonces la propina será alta.

La mayoría de la gente estaría de acuerdo con estas reglas, pero las reglas son confusas. Mapeando el
Reglas imprecisas en una punta definida y procesable es un desafío. Este es el
tipo de tarea en la que sobresale la lógica difusa.
"""

rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

rule1.view()

"""
.. image:: PLOT2RST.current_figure

Control System Creation and Simulation
---------------------------------------

Ahora que tenemos nuestras reglas definidas, simplemente podemos crear un sistema de control
vía:
"""

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

"""
Para simular este sistema de control, crearemos un
`` ControlSystemSimulation ''. Piensa en este objeto que representa nuestro controlador
aplicado a un conjunto específico de circunstancias. Para propinas, esto podría ser propina
Sharon en la cervecería local. Crearíamos otro
`` ControlSystemSimulation`` cuando intentamos aplicar nuestro `` tipping_ctrl``
para Travis en el café porque las entradas serían diferentes.

"""

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

"""
Ahora podemos simular nuestro sistema de control simplemente especificando las entradas
y llamando al método `` calcular ''. Supongamos que calificamos la calidad 6.5 de 10
y el servicio 9.8 de 10.

"""
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

# Crunch the numbers
tipping.compute()

"""
Una vez calculado, podemos ver el resultado y visualizarlo.
"""

