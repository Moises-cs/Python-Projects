from tkinter import *
import time
import random

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
	
	if x == '/':
		while (a % b) != 0:
			a = generar_num()
		
	z = str(a) + x + str(b)
	y = abs(eval(str(a) + x + str(b)))
	return y, z

def Nivel_2():
	a = generar_num()
	b = generar_num()
	c = generar_num()
	x = generar_ope()
	w = generar_ope()
	
	while x == '/' and w == '/':
		x = generar_ope()
		w = generar_ope()
	
	if x == '/':
		while (a % b) != 0:
			a = generar_num()
		
	if w == '/':
		while (b % c) != 0:
			b = generar_num()
		
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
	
	while x == '/' and w == '/':
		w = generar_ope()
	
	while v == '/' and w == '/':
		w = generar_ope()
	
	if x == '/':
		while (a % b) != 0:
			a = generar_num()
		
	if w == '/':
		while (b % c) != 0:
			b = generar_num()
		
	if v == '/':
		while (c % d) != 0:
			c = generar_num()
		
	y = abs(eval(str(a) + x + str(b) + w + str(c) + v + str(d)))
	z = str(a) + x + str(b) + w + str(c) + v + str(d)
	return y, z


def texto(event):
	input = resultado.get()
	resultado.delete(0, END)
	global tiempo
	global cuenta
	global entrada
	global puntuacion
	global nivel
	if nivel == 1:
		if cuenta == int(input):
			respuesta.configure(fg="#32cd32")
			r.set("Correcto")
			puntuacion += 1
			p.set(str(puntuacion))
			cuenta, entrada = Nivel_1()
			o.set(entrada)		
		else:		
			cuenta, entrada = Nivel_1() 
			o.set(entrada)
			respuesta.configure(fg="red")
			r.set("Incorrecto")
	else:
		if nivel == 2:
			if cuenta == int(input):
				respuesta.configure(fg="#32cd32")
				r.set("Correcto")
				puntuacion += 1
				p.set(str(puntuacion))
				cuenta, entrada = Nivel_2()
				o.set(entrada)
			else:		
				cuenta, entrada = Nivel_2() 
				o.set(entrada)
				respuesta.configure(fg="red")
				r.set("Incorrecto")
		else:
			if cuenta == int(input):
				respuesta.configure(fg="#32cd32")
				r.set("Correcto")
				puntuacion += 1
				p.set(str(puntuacion))
				cuenta, entrada = Nivel_3()
				o.set(entrada)
			else:		
				cuenta, entrada = Nivel_3() 
				o.set(entrada)
				respuesta.configure(fg="red")
				r.set("Incorrecto")	
def temporizador():
	global nivel
	global counter
	global puntuacion
	if nivel == 1:
		if	counter <= 0:
			v.set("00")
			resultado.configure(state='disabled')
			if puntuacion >= 10:
				empezar.configure(state='normal')
				nivel = 2
				n.set("NIVEL 2")
				puntuacion = 0
			else:
				o.set("Perdiste")
				puntuacion = 0
				empezar.configure(state='normal')
				nivel = 1
		else:
			v.set(str(counter))
			counter -= 1
			ventana.after(1000, temporizador)
	else:
		if nivel == 2:
			if	counter <= 0:
				v.set("00")
				resultado.configure(state='disabled')
				if puntuacion >= 10:
					empezar.configure(state='normal')
					nivel = 3
					n.set("NIVEL 3")
				else:
					o.set("Perdiste")
					puntuacion = 0
					empezar.configure(state="normal")
					nivel = 1
					n.set("NIVEL 1")
			else:
				v.set(str(counter))
				counter -= 1
				ventana.after(1000, temporizador)	
		else:
			if	counter <= 0:
				v.set("00")
				resultado.configure(state='disabled')
				if puntuacion >= 10:
					empezar.configure(state='normal')
					n.set("Ganaste")
				else:
					o.set("Perdiste")
					empezar.configure(state="normal")
					nivel = 1
					n.set("NIVEL 1")
			else:
				v.set(str(counter))
				counter -= 1
				ventana.after(1000, temporizador)

def iniciar():
	global nivel
	global cuenta
	global entrada
	global tiempo
	global counter
	global puntuacion
	puntuacion = 0
	p.set(puntuacion)
	counter = 30
	resultado.configure(state="normal")
	if nivel == 1:
		cuenta, entrada = Nivel_1()
		o.set(entrada)
		tiempo = True
		temporizador()
		empezar.configure(state='disabled')
	else:	
		if nivel == 2:
			counter = 90
			cuenta, entrada = Nivel_2()
			o.set(entrada)
			tiempo = True
			temporizador()
			empezar.configure(state='disabled')
		else:
			counter = 120
			cuenta, entrada = Nivel_3()
			o.set(entrada)
			tiempo = True
			temporizador()
			empezar.configure(state='disabled')				

fondo = "#483d8b"
letras = "white"			
ventana = Tk()
ventana.title("Quick-Match")
ventana.geometry('300x250')
ventana.config(bg=fondo)

n = StringVar()
v = StringVar()
o = StringVar()
r = StringVar()
p = StringVar()

n.set("NIVEL 1")
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


avance = Label(ventana, textvariable = n,bg = fondo, fg = "Cyan",font=("Helvetica",18))
avance.place(x=10,y=10)
tiempo = Label(ventana,width=5, textvariable = v)
tiempo.place(x=250,y=10)
respuesta = Label(ventana,width=10, textvariable = r, bg = fondo, fg = letras,font=("Helvetica",18))
respuesta.place(x=140,y=200)
puntaje = Label(ventana,width=5, textvariable = p)
puntaje.place(x=250,y=40)
operacion = Label(ventana,width=11, textvariable = o,font=("Helvetica",14))
operacion.place(x=10,y=150)
resultado = Entry(ventana,width=4,font=("Helvetica",18))
resultado.place(x=180,y=150)
resultado.bind('<Return>', texto)
empezar = Button(ventana, text = "Empezar",bg = "#006400", fg = letras,font=("Helvetica",14), command = iniciar)
empezar.place(x=10,y=50)
etiqueta1 = Label(ventana, width=8, text = "Tiempo:")
etiqueta1.place(x=200,y=10)
etiqueta2 = Label(ventana, width=8, text = "Puntaje:")
etiqueta2.place(x=200,y=40)
etiqueta3 = Label(ventana, text = "Resuelve:",bg = fondo, fg = "black",font=("arial",12))
etiqueta3.place(x=10,y=125)
etiqueta4 = Label(ventana, text = "=", bg = fondo, fg = letras,font=("Helvetica",14))
etiqueta4.place(x=150,y=150)

ventana.mainloop()
