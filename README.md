# fuzzyExperto
Utilizando la libreria scikit-fuzzy para crear un sistema experto

## Empezando
Un sistema de audio respuesta tiene un CSV que contiene cantidades de las siguientes variables: llam (frecuencia llamadas), vol (frecuencia de planta telefonica), tran (frecuencia de transacciones)

Se pretende contruir un experto que permita identificar cuando estas variables estan por encima del umbral basandose en una serie de reglas difuzas para determinar si esta por encima o por debajo del umbral.

variables: 
- llam
- tran
- vol

Reglas de negocio:
- lete: llam y tran por encima de lo normal
- leve: llam y vol por encima de lo normal
- le: llam por encima de lo normal
- te: tran por encima de lo normal
- ve: vol por encima de lo normal
- ld: llam por debajo de lo normal
- vt: vol por debajo de lo normal

Fuzzy rules
Ahora, para hacer que estos triángulos sean útiles, definimos la * relación difusa *
entre variables de entrada y salida. Para los propósitos de nuestro ejemplo, considere
seis reglas simples:
```
si lete alto entonces alerta naranja,
si leve alto entonces alerta naranja,
si le alto entonces alerta verde,
si te alto entonces alerta amarilla,
si ve alto entonces alerta verde,
si vd ó td alto entonces alerta verde,
```
```
regla1 = ctrl.Rule(lete['alto'], alerta['naranja'])
regla2 = ctrl.Rule(leve['alto'], alerta['naranja'])
regla3 = ctrl.Rule(le['alto'], alerta['verde'])
regla4 = ctrl.Rule(te['alto'], alerta['amarillo'])
regla5 = ctrl.Rule(ve['alto'], alerta['verde'])
regla6 = ctrl.Rule(vd['alto']  | td['alto'], alerta['verde'])
```

### Prerrequisitos
```
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import pandas as pd
```

## Autores
* **Leonardo Patiño rodriguez** - *Trabajo inicial*

