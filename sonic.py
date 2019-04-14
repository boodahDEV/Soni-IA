import retro
import os
#from Controler_actions import action_control
env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')

f = open ('data.txt','w')

env.reset()
done = False
while not done:
    env.render()
    action = env.action_space.sample()
    action = [0,0,0,0,0,0,0,1,0,0,0,0]
    ob, rew, done, info = env.step(action)
    f.write("\n"+str(action))
    #print("Action: ",info, "\tDone: ", done, "\tOb: ", ob) 

f.close()
#print("que haces:", info)