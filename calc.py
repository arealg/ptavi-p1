#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys


def suma(x, y):
	return x+y


def resta(x, y):
	return x-y


def find_float(sumando):
	if '.' in sumando:
		return float(sumando)
	else:
		return int(sumando)

if __name__ == '__main__':

	sum1 = sys.argv[1]
	sum2 = sys.argv[3]
	operacion = sys.argv[2]

	try:
		numero1 = find_float(sum1)
		numero2 = find_float(sum2)

		if operacion == 'suma':
			print(suma(numero1, numero2))
		elif operacion == 'resta':
			print(resta(numero1, numero2))

	except:
		print ('Error: Non numerical parameters')
