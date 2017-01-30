import time
import random
from sys import exit
continuar = 1
acierto = 0
print ("""
------------------- Bienvenidos a QUICK-MATH -------------------------\n
Se te proporcionaran 30 segundos en cada nivel para resolver la mayor 
cantidad de ejercios matematicos; suma, resta, multiplicacion y division.
\n------------------------  NIVEL 1  ----------------------------------\n""")
	
def generar_num():
	x = random.randint(1,10)
	return x
	
def generar_ope():
	x = random.randint(0,3)
	if x == 0:
		return '+'
	elif x == 1:
		return '-'
	elif x == 2:
		return '*'
	elif x == 3:
		return '/'
	else:
		pass
	
while continuar < 6:
	a = generar_num()
	b = generar_num()
	x = generar_ope()
	modulo = a % b
	while x == '/' and modulo != 0:
		a = generar_num()
		modulo = a % b
		
	y = abs(eval(str(a) + x + str(b)))
	print (str(a)+ x + str(b))
	z = abs(float(input("> ")))
	if z == y:
		acierto += 1
	continuar += 1 

print ("Cantidad de aciertos ",acierto)
print ("\n------------------------  NIVEL 2  ----------------------------------\n")

while continuar < 11:
	a = generar_num()
	b = generar_num()
	c = generar_num()
	x = generar_ope()
	w = generar_ope()
	modulo = a % b
	while x == '/' and (a % b) != 0:
		a = generar_num()
		modulo = a % b
	
	modulo = b % c
	while w == '/' and modulo != 0:
		b = generar_num()
		modulo = b % c
		
	while x == '/' and w == '/':
		x = generar_ope()
		w = generar_ope()
		
	y = abs(eval(str(a) + x + str(b) + w + str(c)))
	print (str(a)+ x + str(b) + w + str(c))
	z = abs(float(input("> ")))
	if z == y:
		acierto += 1
	continuar += 1
	
print ("Cantidad de aciertos ",acierto)
print ("\n------------------------  NIVEL 3  ----------------------------------\n")

while continuar < 16:
	a = generar_num()
	b = generar_num()
	c = generar_num()
	d = generar_num()
	x = generar_ope()
	w = generar_ope()
	v = generar_ope()
	
	modulo = a % b
	while x == '/' and modulo != 0:
		a = generar_num()
		modulo = a % b
	
	modulo = b % c
	while w == '/' and (b % c) != 0:
		b = generar_num()
		
	modulo = c % d
	while v == '/' and modulo != 0:
		c = generar_num()
		modulo = c % d
		
	while x == '/' and w == '/':
		w = generar_ope()
	
	while v == '/' and w == '/':
		w = generar_ope()
		
	y = abs(eval(str(a) + x + str(b) + w + str(c) + v + str(d)))
	print (str(a)+ x + str(b) + w + str(c) + v + str(d))
	z = abs(float(input("> ")))
	if z == y:
		acierto += 1
	continuar += 1

print ("Cantidad de aciertos ",acierto)
