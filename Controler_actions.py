from tkinter import *


def action_control(action):
    


def keyup(e):
	if e.keysym == 'Escape': 
		root.quit()
		#print("up", e.char)
	if e.keysym == 'Right': 
		print("Derecha ", e.char)
	if e.keysym == 'Left': 
		print("Izquierda", e.char)
	if e.keysym == 'Up': 
		print("Arriba", e.char)
	if e.keysym == 'Down': 
		print("Abajo", e.char)
	if e.keysym == 'Shift_L': 
		print("Shift_L")
	while e.keysym == 'Shift_L' and e.keysym == 'Right':
		print("Right")

root = Tk()
root.title("Controller_actions_button_bj")
fx = Frame(root, width=0, height=0)
fx.bind_all('<Key>', keyup) #llamada de los botones
fx.pack() #Empaqueta todo y lanza
fx.focus_set() #seteo el foco a la ventana(mucho mejor)
root.mainloop()