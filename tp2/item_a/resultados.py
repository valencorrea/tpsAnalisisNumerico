from item_a.runge_kutta import runge_kutta_orden4 as runge
from item_a.funciones import derivada_x
from item_a.funciones import derivada_y
import pandas as pd

# N = tiempo / paso = 30 / 0.1 = 300
resultados = runge(derivada_x, derivada_y, 0, 2, 1, 0.1, 300)

tiempo = resultados[:,0]
presa = resultados[:,1]
depredador = resultados[:,2]

tabla = {'tiempo': tiempo, 'presa': presa, 'depredador': depredador}
df1 = pd.DataFrame(tabla, columns = ['tiempo', 'presa', 'depredador'])
df1.to_csv("resultados_item_a.csv", float_format='{0:.7f}'.format)