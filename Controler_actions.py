from tkinter import *
import retro
#from Controler_actions import action_control
env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')
root = Tk()

action = env.action_space.sample()
env.reset()

def action_control(action):
    
    def keyup(e):
        if e.keysym == 'Escape': 
            root.quit()
            #print("up", e.char)
        if e.keysym == 'Right': 
            action = [0,0,0,0,0,0,0,1,0,0,0,0]
            print("Derecha ", e.char)
            return action
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

    root.title("Controler_actions_button_bj")
    fx = Frame(root, width=0, height=0)
    fx.pack() #Empaqueta todo y lanza
    fx.focus_set() #seteo el foco a la ventana(mucho mejor)
    root.mainloop()
    done = False 
    while not done:
        fx.bind_all('<Key>', keyup) #llamada de los botones
   
    ob, rew, done, info = env.step(action)

action_control(action) ## llama el controlador



