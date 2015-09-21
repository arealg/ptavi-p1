#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys

def suma(x,y):
	return x+y

def resta(x,y):
    return x-y


sum1 = sys.argv[1]
sum2 = sys.argv[3]
operacion = sys.argv[2]

operando1 = sum1.find('.')
operando2 = sum2.find('.')

try:
    if operando1 and operando2 == 1:
        sum1 = float(sys.argv[1])
        sum2 = float(sys.argv[3])
    elif operando1 == 1 and operando2 == -1:
        sum1 = float(sys.argv[1])
        sum2 = int(sys.argv[3])
    elif operando1 == -1 and operando2 == 1:
        sum1 = int(sys.argv[1])
        sum2 = float(sys.argv[3])
    elif operando1 and operando2 == -1:
        sum1 = int(sys.argv[1])
        sum2 = int(sys.argv[3])

    if operacion == 'suma':
        print(suma(sum1,sum2))
    elif operacion == 'resta':
        print(resta(sum1,sum2))

except:
    print ('Error')
