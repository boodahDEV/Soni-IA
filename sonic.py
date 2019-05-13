import retro
import os
#from Controler_actions import action_control
env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')

f = open ('data.csv','w')

env.reset()
done = False
while not done:
    env.render()
    action = env.action_space.sample()
    action = [0,0,0,0,0,0,0,1,0,0,0,0]
    ob, rew, done, info = env.step(action)
    f.write("\n"+str(info))
    #ob es la imagen de la pantalla en el momento de la accion
    #done es para saber suantas vidas tiene o que, osea si muere done == true se cierra el bucle!
    #info es un diccionario de todos los valores establecidos en los datos correctos.
    print("Image: ",ob.shape,"\tReward: ",rew, "\tDone: ", done, "\t actions: ", action) 
    

f.close()
#print("que haces:", info)