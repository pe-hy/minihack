import gym
import minihack
import gym

import gym
import minihack

DES_FILE = """
MAZE: "mylevel",' '
GEOMETRY:center,center
MAP
-------------
|.....|.....|
|.....|.....|
|.....+.....|
|.....|.....|
|.....|.....|
-------------
ENDMAP
REGION:(0,0,12,6),lit,"ordinary"
BRANCH:(1,1,6,6),(0,0,0,0)
DOOR:locked,(6,3)
STAIR:(8,3),down
"""

def test_run():
    env = gym.make(
        "MiniHack-Navigation-Custom-v0",
        des_file=DES_FILE,
        max_episode_steps=100,
    )
    env.reset()
    env.render(mode="human")

    obs = env.reset()

    for _ in range(1000):
        next_obs, reward, done, info = env.step(env.action_space.sample())

        env.render(mode="human")

        obs = next_obs
        if done:
            obs = env.reset()



if __name__ == '__main__':
    test_run()
