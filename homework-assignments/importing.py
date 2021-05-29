# Programming Course: Python is Easy by pirple.com
# Homework assignment: Importing
# Written by Franz Tapia Chaca
# Last updated 30 May 2021

# Learning how to extensively use matplotlib
# Executing examples provided at https://matplotlib.org/stable/tutorials/index.html

##############################
# Learning to use MATPLOTLIB #
##############################

import matplotlib.pyplot as plt  # a module
import numpy as np

# # Creating a simple figure
# fig, ax = plt.subplots()  # figure with single axes
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
# plt.show()

# The figure
#   - keeps track of child Axes, figure parts and the canvas
#   - has any number of Axes, at least 1
# fig = plt.figure()              # empty figure with no Axes
# fig, ax = plt.subplots()        # figure with single Axes
# fix, axs = plt.subplots(2, 2)    # figure with 2x2 grid of Axes (i.e. 4 subplots)
# plt.show()

# Axes
#   - the "plot"
#   - a given Axes object can only be in one Figure
#   - contains 2 Axis objects (for 2D)

# Axis
#   - Number-line-like objects
#   - Takes care of setting graph limits, ticks and tick labels

# Artist
#   - Everything seen on the figure is an artist (including Figure, Axes, Axis objects)
#   - Also Text, Line2D, collections, Patch, ... objects

# Canvas
#   - When figure is rendered, all artists are drawn to the canvas
#   - Artists tied to an Axes cannot be shared by multiple Axes, or moved from one to another

# Types of inputs to plotting functions
#   - Almost all functions expect input
#   - Array-like functions (pandas, numpy.matrix): best to convert to numpy.array before plotting

# Object-oriented interface and pyplot interface
#   1) OO-style: explicitly create figures and axes, and call methods on them
#   2) pyplot-style: pyplot automatically creates and manages figures and axes. You use pyplot functions for plotting

# Object-oriented style
# x = np.linspace(0, 2, 100)  # 100 samples [0, 2], inclusive
#
# fig, ax = plt.subplots()
# ax.plot(x, x, label='linear')
# ax.plot(x, x**2, label='quadratic')
# ax.plot(x, x**3, label='cubic')
# ax.set_xlabel('x label')
# ax.set_ylabel('y label')
# ax.set_title('Simple plot')
# ax.legend()
# plt.show()
#
# # Pyplot-style
# x = np.linspace(0, 2, 100)
# plt.plot(x, x, label='linear')  # data plotted on implicit axes
# plt.plot(x, x**2, label='quadratic')
# plt.plot(x, x**3, label='cubic')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title('Simple plot')
# plt.legend()
# plt.show()

# 3rd approach
# for when embedding Matplotlib in a GUI application
# https://matplotlib.org/stable/gallery/index.html#user-interfaces


# Suggestions for approach use:
#   pyplot:     interactive plotting (e.g. in a Jupyter notebook)
#   OO-style:   for non-interactive plotting (in functions and scripts intended to be reused, e.g. in a large project)


# Pylab - discouraged and deprecated
# from pylab import *  # imports everything from pyplot and numpy for a MATLAB style lab
# x = linspace(0, 2 ,100)
# plot(x, x, label='linear')
# show


# Plotting function
# def my_plotter(ax, data1, data2, param_dict):
#     out = ax.plot(data1, data2, **param_dict)
#     return out
#
#
# data1, data2, data3, data4 = np.random.randn(4, 100)
# fig, ax = plt.subplots(1, 1)
# my_plotter(ax, data1, data2, {'marker': 'x'})
# plt.show()

# fig, (ax1, ax2) = plt.subplots(1, 2)
# my_plotter(ax1, data1, data2, {'marker': 'x'})
# my_plotter(ax2, data3, data4, {'marker': 'o'})
# plt.show()


# Backends