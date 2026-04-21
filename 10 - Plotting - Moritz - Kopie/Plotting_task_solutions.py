# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:31:10 2026

@author: nesseler
"""

# %% Scatter plot task

import matplotlib.pyplot as plt
import random

x = random.sample(range(0, 101), 50)
y = random.sample(range(0, 101), 50)

plt.scatter(x, y, label = 'data1')

plt.xlim([0, 100])
plt.xlabel('x axis')

plt.ylim([0, 100])
plt.ylabel('y axis')

ax = plt.gca()
ax.set_aspect(1)

x2 = random.sample(range(0, 101), 50)
y2 = random.sample(range(0, 101), 50)

plt.scatter(x2, y2, color = 'r', label = 'data2')

plt.legend(loc = 'lower right')

plt.show()


# %% histogram task

import numpy as np

mu = 50
sd = 10
data = np.random.normal(mu, sd, 1000)

mu2 = 60
data2 = np.random.normal(mu2, sd, 1000)

fig, ax = plt.subplots()

ax.hist(data, bins=50, label = 'data1', edgecolor = 'b', facecolor = 'w')
ax.hist(data2, bins=50, label = 'data2', edgecolor = 'r', facecolor = 'w')

ax.set_title(f'random gaussian distributions\nwith mean of {mu} or {mu2} and std of {sd}')

ax.set_xlim([0, 100])
ax.set_xticks(np.arange(0, 100+1, 10))
ax.set_xticks(np.arange(0, 100+1, 5), minor = True)
ax.set_xlabel('x axis')

ax.set_ylim([0, 80])
ax.set_yticks(np.arange(0, 80+1, 20))
ax.set_ylabel('y axis')

plt.show()


# %% time series task

import pandas as pd

data_path = 'E320_ccIF.csv'
ccIF = pd.read_csv(data_path, header=None)
t = np.arange(0, 1.5, 1/(50*1e3))

step = 13

fig, ax = plt.subplots()

ax.plot(t, ccIF[step])

ax.plot([0, 1.5], [-85, -85], lw = 1, c = 'k', alpha = 0.5, ls = 'dashed')

ax.set_xlim([0, 1.5])
ax.set_xticks(np.arange(0, 1.5+0.1, 0.25))
ax.set_xticks(np.arange(0, 1.5+0.01, 0.1), minor = True)
ax.set_xlabel('time [s]')

ax.set_ylim([-100, 70])
ax.set_yticks(np.arange(-100, 70, 20))
ax.set_yticks(np.arange(-100, 70, 5), minor = True)
ax.set_ylabel('voltage [mV]')

plt.show()

# %% time series task - loop

for step in range(ccIF.shape[1]):
    fig, ax = plt.subplots()

    ax.plot(t, ccIF[step])
    
    ax.plot([0, 1.5], [-85, -85], lw = 1, c = 'k', alpha = 0.5, ls = 'dashed')
    
    ax.set_xlim([0, 1.5])
    ax.set_xticks(np.arange(0, 1.5+0.1, 0.25))
    ax.set_xticks(np.arange(0, 1.5+0.01, 0.1), minor = True)
    ax.set_xlabel('time [s]')
    
    ax.set_ylim([-100, 70])
    ax.set_yticks(np.arange(-100, 70, 20))
    ax.set_yticks(np.arange(-100, 70, 5), minor = True)
    ax.set_ylabel('voltage [mV]')
    
    plt.show()

# %% time series task - Combine Plots

fig, ax = plt.subplots()

for step in range(ccIF.shape[1]):
    ax.plot(t, ccIF[step], alpha = 0.05, c = 'k')

ax.plot(t, ccIF[4], c='k')
ax.plot([0, 1.5], [-85, -85], lw = 1, c = 'k', alpha = 0.5, ls = 'dashed')

ax.set_xlim([0, 1.5])
ax.set_xticks(np.arange(0, 1.5+0.1, 0.25))
ax.set_xticks(np.arange(0, 1.5+0.01, 0.1), minor = True)
ax.set_xlabel('time [s]')

ax.set_ylim([-100, 70])
ax.set_yticks(np.arange(-100, 70, 20))
ax.set_yticks(np.arange(-100, 70, 5), minor = True)
ax.set_ylabel('voltage [mV]')

plt.show()


# %% time series task - Subplots

fig, axs = plt.subplots(nrows = 4, ncols = 6,
                        layout = 'constrained',
                        sharex=True,
                        sharey=True,
                        figsize = [13.333, 7.5])

axs = axs.flatten()

for step in range(ccIF.shape[1]):
    
    ax = axs[step]
    
    ax.plot(t, ccIF[step], c = 'k', lw = 0.75)
    ax.plot([0, 1.5], [-85, -85], lw = 1, c = 'k', alpha = 0.5, ls = 'dashed')


ax.set_xlim([0, 1.5])
ax.set_xticks(np.arange(0, 1.5+0.1, 1.5))
ax.set_xticks(np.arange(0, 1.5+0.01, 0.1), minor = True)

ax.set_ylim([-100, 70])
ax.set_yticks(np.arange(-100, 70, 50))
ax.set_yticks(np.arange(-100, 70, 5), minor = True)

fig.supxlabel('time [s]')
fig.supylabel('voltage [mV]')

plt.show()



# %% Seaborn task

import seaborn as sns

df = sns.load_dataset("penguins")

# 3.a
sns.histplot(df, 
             x="flipper_length_mm", 
             hue="species", 
             element="step")
plt.show()

# 3.b
sns.violinplot(df, 
               x = 'species',
               y = 'flipper_length_mm',
               hue = 'sex',
               dodge = True)
plt.show()

#3.c
sns.swarmplot(df,
              x = 'species', 
              y = 'body_mass_g',
              hue = 'sex',
              dodge = True)
plt.show()


# 3.d
sns.jointplot(df, 
              x='flipper_length_mm', 
              y='bill_length_mm', 
              hue='island')
plt.show()
