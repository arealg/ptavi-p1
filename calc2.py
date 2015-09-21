#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys

def suma(x,y):
	return x+y

def resta(x,y):
    return x-y

print (sys.argv)

try:
	sum1 = float(sys.argv[1])
	sum2 = float(sys.argv[3])
	operacion = sys.argv[2]

	if operacion == 'suma':
		print (suma(sum1,sum2))
	elif operacion == 'resta':
		print(resta(sum1,sum2))
except:
	print ('Error')
