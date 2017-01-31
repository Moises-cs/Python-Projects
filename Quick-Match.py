from Tkinter import *
import time
import random
from sys import exit
def texto(event):
	input = resultado.get()
	resultado.delete(0, END)
	global cuenta
	global entrada
	global puntuacion
	if cuenta == int(input):
		r.set("Correcto")
		puntuacion += 1
		p.set(str(puntuacion))
		cuenta, entrada = Nivel_1()
		o.set(entrada)
	else:
		cuenta, entrada = Nivel_1()
		o.set(entrada)		
def iniciar():
	global nivel
	global cuenta
	global entrada
	global tiempo
	cuenta, entrada = Nivel_1()
	o.set(entrada)
	tiempo = True
	temporizador()
	empezar.configure(state='disabled')
	
def temporizador():
	if tiempo ==  True:
		global counter
		if puntuacion >= 5:
			v.set("Pasaste!")
			resultado.configure(state='disabled')
		else:
			if	counter <= 0:
				v.set("tiempo")
				resultado.configure(state='disabled')
			else:
				v.set(str(counter))
				counter -= 1
				ventana.after(1000, temporizador)
	
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
	
def Nivel_1(): 
	a = generar_num()
	b = generar_num()
	x = generar_ope()
	
	while x == '/' and (a % b) != 0:
		a = generar_num()
		
	y = abs(eval(str(a) + x + str(b)))
	z = str(a) + x + str(b)
	if z == y:
		acierto += 1
	return y, z

#lista = Nivel_1()       #los valores devueltos por Nivel_1 se pueden guardar en una lista
#print (lista[1],lista[0]) #Accde por separado para que lo pongas en tus label
	
def Nivel_2():
	a = generar_num()
	b = generar_num()
	c = generar_num()
	x = generar_ope()
	w = generar_ope()
	
	while x == '/' and (a % b) != 0:
		a = generar_num()
		
	while w == '/' and (b % c) != 0:
		b = generar_num()
		
	while x == '/' and w == '/':
		x = generar_ope()
		w = generar_ope()
		
	y = abs(eval(str(a) + x + str(b) + w + str(c)))
	z = str(a) + x + str(b) + w + str(c)
	return y, z
	
def Nivel_3():
	a = generar_num()
	b = generar_num()
	c = generar_num()
	d = generar_num()
	x = generar_ope()
	w = generar_ope()
	v = generar_ope()
	
	while x == '/' and (a % b) != 0:
		a = generar_num()
		
	while w == '/' and (b % c) != 0:
		b = generar_num()
		
	while v == '/' and (c % d) != 0:
		c = generar_num()
		
	while x == '/' and w == '/':
		w = generar_ope()
	
	while v == '/' and w == '/':
		w = generar_ope()
		
	y = abs(eval(str(a) + x + str(b) + w + str(c) + v + str(d)))
	
	z = str(a) + x + str(b) + w + str(c) + v + str(d)
	return y, z				

ventana = Tk()
ventana.geometry('300x200')

n = StringVar()
v = StringVar()
o = StringVar()
r = StringVar()
p = StringVar()

n.set("Nivel 1")
v.set("30")
o.set(" ")
r.set(" ")
p.set("0")


counter = 30
nivel = 1
tiempo = False
cuenta = 0
entrada = " "
puntuacion = 0

nivel = Label(ventana, textvariable = n)
nivel.pack()
tiempo = Label(ventana, textvariable = v)
tiempo.pack()
respuesta = Label(ventana, textvariable = r)
respuesta.pack()
puntaje = Label(ventana, textvariable = p)
puntaje.pack()
operacion = Label(ventana, textvariable = o)
operacion.pack()
resultado = Entry(ventana)
resultado.pack()
resultado.bind('<Return>', texto)
empezar = Button(ventana, text = "Empezar", command = iniciar)
empezar.pack()
ventana.mainloop()
