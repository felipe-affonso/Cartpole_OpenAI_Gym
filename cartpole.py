#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 13:12:57 2018

@author: FelipeAffonso
"""

import gym
import numpy as np
import matplotlib as plt
n_episodes = 200
env_vis = []

env = gym.make('CartPole-v0')
for i_episode in range(n_episodes):
    observation = env.reset()
    for t in range(100):
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode  finished  at  t{}".format(t+1))
            break


def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    for _ in range(500):
        action = 0 if np.matmul(parameters, observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        #print(observation)
        totalreward += reward
        if done:
            break
    return totalreward


        
for i_episode in range(n_episodes):
    bestparams = None
    bestreward = 0
    for t in range(10000):
        env.render()
        parameters = np.random.rand(4)*2 -1
        reward = run_episode(env, parameters)
        if reward > bestreward:
            bestreward = reward
            bestparams = parameters
            if reward == 200:
                print('Got here t{}'.format(t+1))
                break
        if done:
            #print("Episode finished after {} timesteps".format(t+1))
            print('nooooo t{}'.format(t+1))
            break
    
