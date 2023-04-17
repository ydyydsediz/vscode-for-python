import gym
import time
env = gym.make('CartPole-v1', render_mode="human")
for episode in range(100):
    env.reset()
    print("Episode finished after {} timesteps".format(episode))
    print('----------')
    for ik in range(20):
        env.render()
        observation, reward, done, info, _ = env.step(
            env.action_space.sample())
        if done:
            print(reward)
            break
        time.sleep(0.02)
env.close()
