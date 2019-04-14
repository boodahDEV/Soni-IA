from tkinter import *

ap = []

moverderecha = moverizquierda = moverarriba = moverabajo=False
def decision(e=None):
	if e.keysym == 'Right' and e.keysym == 'Up':
		print("Hola")

def keyup(e):
	if e.keysym == 'Escape': 
		root.quit()
		#print("up", e.char)
	if e.keysym == 'Right': 
		moverizquierda = False
		moverderecha = True
		print(moverderecha)
		ap = [0,0,0,0,0,0,0,1,0,0,0,0]
	if e.keysym == 'Left': 
		moverderecha = False
		moverizquierda = True
		print(moverizquierda)
		ap = [0,0,0,0,0,0,1,0,0,0,0,0]
	if e.keysym == 'Up': 
		moverabajo = False
		moverarriba = True
		print(moverarriba)
		ap = [0,0,0,0,0,0,0,0,1,0,0,0]
	if e.keysym == 'Down': 
		moverarriba = False
		moverabajo = True
		print(moverabajo)
		ap = [0,0,0,0,0,1,0,0,0,0,0,0]
	if e.keysym == 'Shift_L': 
		print("Shift_L")
root = Tk()
root.title("Controller_actions_button_bj")
fx = Frame(root, width=0, height=0)
fx.bind_all('<KeyRelease>', keyup) #llamada de los botones
fx.bind_all('<Right-Up>', decision)
fx.pack() #Empaqueta todo y lanza
fx.focus_set() #seteo el foco a la ventana(mucho mejor)
root.mainloop() 

