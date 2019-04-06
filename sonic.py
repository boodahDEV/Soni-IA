import retro
env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')

env.reset()
done = False
while not done:
    env.render()

    action = env.action_space.sample()
    ob, rew, done, info = env.step(action)
   # test = env.controller_bj_action().
   # print("Action ", action, "Reward ", rew) 
print(info)