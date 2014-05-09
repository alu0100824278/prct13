#!/usr/bin/python
#!encoding: UTF-8

import time
import modulo_1
import matplotlib.pyplot as mp

inicio = time.time()

a=[]
b=[]

def error(n_int,n_test,umbral):
  fallo = 0.0
  for i in range (n_test):
    s = modulo_1.aprox(n_int)
    error = abs( s - modulo_1.PI)
    if error >= umbral:
      fallo = fallo + 1
  return ((fallo/n_test)*100)

n_upla = (10,50,100,150, 500, 650, 1000)
for i in range(len(n_upla)):
  s = error(n_upla[i],5,0.01)
  b = b + [s]
  print "El porcentaje de error es de: %f \n" % s
  fin = time.time()
  total = fin - inicio
  a = a + [total]
print ('El tiempos que demoró la ejecución son de: \n')
print a

c = []
for i in range(len(n_upla)):
  c = c + [n_upla[i]]

mp.figure(figsize=(8,6), dpi=80)
grafica1 = mp.subplot(211)
mp.plot(a, c, 'm', marker='h')
mp.ylabel('Tiempo empleado (segundos)')
mp.xlabel('Intervalos')
mp.title('Tiempo frente a los intervalos')
mp.xlim(0.0, 0.003)
mp.ylim(0.0, 1000.0)
mp.legend(['Tiempos'], loc = 2, numpoints = 3)
grafica2 = mp.subplot(212)
mp.plot(c, b, 'c', marker='h')
mp.ylabel('Porcentaje de error')
mp.xlabel('Intervalos')
mp.title('Porcentaje de error frente a los intervalos')
mp.xlim(0,0,1.0)
mp.ylim(-0.5,1000.0)
mp.legend(['Porcentajes'], loc = 2, numpoints = 3)
mp.savefig('figura.png',dpi = 200)
mp.show()