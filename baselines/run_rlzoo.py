from common.env_wrappers import *
from common.utils import *
from algorithms import *

# EnvName = 'CartPole-v1'
# EnvType = ['classic_control', 'atari', 'box2d', 'mujoco', 'dm_control'][0]

# env = build_env(EnvName, EnvType)
# alg_params, learn_params = call_default_params(env, EnvType, 'DQN')
# alg = DQN('train', **alg_params)
# alg.learn(env=env, number_timesteps=int(1e4), save_path=None,
#           save_interval=0, **learn_params)


# EnvName = 'CartPole-v0'
# EnvType = ['classic_control', 'atari', 'box2d', 'mujoco', 'dm_control'][0]

# env = build_env(EnvName, EnvType)
# alg_params, learn_params = call_default_params(env, EnvType, 'AC')
# alg = AC(**alg_params)
# alg.learn(env=env, train_episodes=1000, test_episodes=1000, 
#         save_interval=100, mode='train', render=False, **learn_params)


# EnvName = 'CartPole-v1'
# EnvType = ['classic_control', 'atari', 'box2d', 'mujoco', 'dm_control'][0]

# env = build_env(EnvName, EnvType)
# alg_params, learn_params = call_default_params(env, EnvType, 'PG')
# alg = PG(**alg_params)
# alg.learn(env=env, train_episodes=1000, test_episodes=1000, 
#         save_interval=100, mode='train', render=False, **learn_params)


# EnvName = 'Pendulum-v0'
# EnvType = ['classic_control', 'atari', 'box2d', 'mujoco', 'dm_control'][0]

# env = build_env(EnvName, EnvType)
# alg_params, learn_params = call_default_params(env, EnvType, 'SAC')
# alg = SAC(**alg_params)
# alg.learn(env=env, train_episodes=1000, test_episodes=1000, 
#         save_interval=100, mode='train', render=False, **learn_params)


EnvName = 'Pendulum-v0'
EnvType = ['classic_control', 'atari', 'box2d', 'mujoco', 'dm_control'][0]

env = build_env(EnvName, EnvType)
alg_params, learn_params = call_default_params(env, EnvType, 'TD3')
alg = TD3(**alg_params)
alg.learn(env=env, train_episodes=1000, test_episodes=1000, 
        save_interval=100, mode='train', render=False, **learn_params)
