from Tkinter import *
import time
import random

def texto(event):				#Funciona al presionar Enter despues de insertar una respuesta en el box(resultado) #
	input = resultado.get()			#Guarda la respuesta del usuario, limpia el box(resultado), compara respuestas, ...
	resultado.delete(0, END)		#...si la respuesta es correcta: manda un mensaje "correcto" en label(respuesta)...
	global cuenta				#...actualiza la puntuacion en label(puntaje), llama la funcion Nivel_1(), y    ...
	global entrada				#...muestra la nueva operacion en label(operacion)                                  #
	global puntuacion
	if cuenta == int(input):
		r.set("Correcto")
		puntuacion += 1
		p.set(str(puntuacion))
		cuenta, entrada = Nivel_1()
		o.set(entrada)					

def iniciar():					#Funciona al presionar el boton Empezar
	global nivel
	global cuenta
	global entrada
	global tiempo
	cuenta, entrada = Nivel_1()
	o.set(entrada)
	tiempo = True
	temporizador()
	empezar.configure(state='disabled')
	
def temporizador():				#Funciona al llamar la funcion iniciar()
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
